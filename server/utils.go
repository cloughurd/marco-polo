package server

import "database/sql"

func TableExistsInDb(db *sql.DB, tableName string) (bool, error) {
	err := db.Ping()
	if err != nil {
		return false, err
	}
	row := db.QueryRow("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name=?", tableName)
	var numTables int
	err = row.Scan(&numTables)
	if (err != nil) || (numTables < 1) {
		return false, err
	} else {
		return true, nil
	}
}
