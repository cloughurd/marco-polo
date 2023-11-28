package game

import (
	"database/sql"
	"errors"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/marco-polo/server"
)

type state struct {
	ID       string   `json:"id"`
	Name     string   `json:"name"`
	Capital  string   `json:"capital"`
	CityList []string `json:"cityList"`
}

type StateHandler struct {
	db *sql.DB
}

func InitStateHandler(db *sql.DB) (*StateHandler, error) {
	tableExists, err := server.TableExistsInDb(db, "state")
	if err != nil {
		return &StateHandler{}, err
	}
	if !tableExists {
		return &StateHandler{}, errors.New("The database does not contain the 'state' table, which is required for handling requests to /state endpoints")
	}
	tableExists, err = server.TableExistsInDb(db, "city")
	if err != nil {
		return &StateHandler{}, err
	}
	if !tableExists {
		return &StateHandler{}, errors.New("The database does not contain the 'city' table, which is required for handling requests to /state endpoints")
	}
	return &StateHandler{db: db}, nil
}

func (h *StateHandler) GetStates(c *gin.Context) {
	param, ok := c.GetQuery("includeCities")
	var states []state
	var err error
	if (ok) && (param == "true") {
		states, err = h.getStates(true)
	} else {
		states, err = h.getStates(false)
	}
	if err != nil {
		c.AbortWithError(http.StatusInternalServerError, err)
	}
	c.IndentedJSON(http.StatusOK, states)
}

func (h *StateHandler) getStates(includeCities bool) ([]state, error) {
	var states []state
	query := "SELECT state.id, state.name FROM state"
	rows, err := h.db.Query(query)
	if err != nil {
		return nil, err
	}
	for rows.Next() {
		s := state{}
		err = rows.Scan(&s.ID, &s.Name)
		if err != nil {
			return nil, err
		}
		states = append(states, s)
	}
	if includeCities {
		for i := 0; i < len(states); i++ {
			capital, cityList, err := h.getCities(states[i].ID)
			if err != nil {
				return nil, err
			}
			states[i].Capital = capital
			states[i].CityList = cityList
		}
	}

	return states, nil
}

func (h *StateHandler) getCities(stateID string) (string, []string, error) {
	var capital string
	var cityList []string
	query := "SELECT name, is_capital FROM city WHERE state_id = '?'"
	rows, err := h.db.Query(query, stateID)
	if err != nil {
		return "", nil, err
	}
	for rows.Next() {
		var cityName string
		var isCapital int
		err = rows.Scan(&cityName, &isCapital)
		if err != nil {
			return "", nil, err
		}
		if isCapital == 1 {
			capital = cityName
		} else {
			cityList = append(cityList, cityName)
		}
	}
	if capital == "" {
		return "", nil, errors.New(fmt.Sprintf("No capital was found for '%s'", stateID))
	}
	return capital, cityList, nil
}

func (h *StateHandler) GetStateFact(c *gin.Context) {
	state := c.Param("abbreviation")
	if state == "michigan" {
		c.IndentedJSON(http.StatusOK, gin.H{"message": "The lower peninsula is shaped like a mitten."})
	} else {
		c.IndentedJSON(http.StatusNotImplemented, gin.H{"message": "I don't know any fun facts about that state."})
	}
}
