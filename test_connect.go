package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
	"go.bmvs.io/ynab"
)


func get_access_token() string {
	api_key, err := ioutil.ReadFile("./api_key")
	if err != nil {
		log.Fatalf("unable to read file: %v", err)
	}
	fmt.Println(api_key)
	return strings.TrimSuffix(string(api_key), "\n")
}

func main() {
	
	accessToken := get_access_token()

	c := ynab.NewClient(accessToken)
	budgets, err := c.Budget().GetBudgets()
	if err != nil {
		panic(err)
	}

	for _, budget := range budgets {
		fmt.Println(budget.Name)
		// ...
	}
}
