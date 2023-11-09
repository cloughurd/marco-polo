package main

import (
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/marco-polo/server/game"
)

func main() {
	router := gin.Default()
	router.GET("/status", healthcheck)

	err := game.InitStates()
	if err != nil {
		log.Fatal("Error initializing the capitals game: ", err)
	}
	router.GET("/states", game.GetStates)

	router.Run("localhost:8080")
}

func healthcheck(c *gin.Context) {
	c.Status(http.StatusOK)
}
