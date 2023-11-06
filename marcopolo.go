package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/marco-polo/server/game"
)

func main() {
	router := gin.Default()
	router.GET("/status", healthcheck)

	router.GET("/states", game.GetStates)

	router.Run("localhost:8080")
}

func healthcheck(c *gin.Context) {
	c.Status(http.StatusOK)
}
