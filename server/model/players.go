package model

type player struct {
	Name        string `json:"name"`
	Catchphrase string `json:"catchphrase"`
}

type game struct {
	Name string `json:"name"`
}

type score struct {
	Player player  `json:"player"`
	Game   game    `json:"game"`
	Score  float64 `json:"score"`
}
