package server

import "database/sql"

type handler struct {
	db *sql.DB
}
