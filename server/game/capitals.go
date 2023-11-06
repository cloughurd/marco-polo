package game

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type state struct {
	Name         string `json:"name"`
	Capital      string `json:"capital"`
	Abbreviation string `json:"abbreviation"`
}

var states = []state{
	{Name: "Wisconsin", Capital: "Madison", Abbreviation: "WI"},
	{Name: "Utah", Capital: "Salt Lake City", Abbreviation: "UT"},
	{Name: "Michigan", Capital: "Lansing", Abbreviation: "MI"},
}

func GetStates(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, states)
}
