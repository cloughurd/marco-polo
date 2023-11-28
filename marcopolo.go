package main

import (
	"database/sql"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/marco-polo/server/game"
	_ "github.com/mattn/go-sqlite3"
)

const dbFile string = "resources/marcopolo.db"

func main() {
	router := gin.Default()
	router.GET("/status", healthcheck)

	db, err := sql.Open("sqlite3", dbFile)
	if err != nil {
		log.Fatal("Error connecting to the database: ", err)
	}
	stateHandler, err := game.InitStateHandler(db)
	if err != nil {
		log.Fatal("Error initializing the capitals game: ", err)
	}
	router.GET("/states", stateHandler.GetStates)
	router.GET("/state/:id/fact", stateHandler.GetStateFact)

	router.Run("localhost:8080")
}

func healthcheck(c *gin.Context) {
	c.Status(http.StatusOK)
}
