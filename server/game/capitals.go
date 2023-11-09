package game

import (
	"encoding/json"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

type state struct {
	Name     string   `json:"name"`
	Capital  string   `json:"capital"`
	CityList []string `json:"cityList"`
}

var states []state

func InitStates() error {
	content, err := os.ReadFile("./resources/states.json")
	if err != nil {
		return err
	}

	err = json.Unmarshal(content, &states)
	if err != nil {
		return err
	}
	return nil
}

func GetStates(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, states)
}
