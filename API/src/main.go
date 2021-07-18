package main

import (
	"context"
	"log"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo/options"
)

const dbName = "cabasdat"
const port = 8000
const collectionName = "hospital"

func GetAllHospitals(c *gin.Context) {
	allHospital := []Hospital{}
	collection, _ := getMongoDbCollection(dbName, collectionName)
	cursor, err := collection.Find(context.TODO(), bson.M{})
	if err != nil {
		log.Printf("Error while getting all hospitals, Reason: %v\n", err)
		c.JSON(http.StatusInternalServerError, gin.H{
			"status":  http.StatusInternalServerError,
			"message": "Something went wrong",
		})
		return
	}
	// Iterate through the returned cursor.
	for cursor.Next(context.TODO()) {
		var hospital Hospital
		cursor.Decode(&hospital)
		allHospital = append(allHospital, hospital)
	}
	c.JSON(http.StatusOK, gin.H{
		"status": http.StatusOK,
		"data":   allHospital,
	})
	return
}

func GetHospitalByProvince(c *gin.Context) {
	id, _ := strconv.Atoi(c.Param("id"))
	allHospital := []Hospital{}
	collection, _ := getMongoDbCollection(dbName, collectionName)
	cursor, err := collection.Find(context.TODO(), bson.M{"provinceId": id})
	if err != nil {
		log.Printf("Error while getting all hospitals, Reason: %v\n", err)
		c.JSON(http.StatusInternalServerError, gin.H{
			"status":  http.StatusInternalServerError,
			"message": "Something went wrong",
		})
		return
	}
	// Iterate through the returned cursor.
	for cursor.Next(context.TODO()) {
		var hospital Hospital
		cursor.Decode(&hospital)
		allHospital = append(allHospital, hospital)
	}
	c.JSON(http.StatusOK, gin.H{
		"status": http.StatusOK,
		"data":   allHospital,
	})
	return
}

func GetProvinces(c *gin.Context) {
	allProvince := []Province{}
	collection, _ := getMongoDbCollection(dbName, "province")
	opts := options.Find()
	opts.SetSort(bson.D{{"provinceId", 1}})
	cursor, err := collection.Find(context.TODO(), bson.M{}, opts)
	if err != nil {
		log.Printf("Error while getting all hospitals, Reason: %v\n", err)
		c.JSON(http.StatusInternalServerError, gin.H{
			"status":  http.StatusInternalServerError,
			"message": "Something went wrong",
		})
		return
	}
	// Iterate through the returned cursor.
	for cursor.Next(context.TODO()) {
		var province Province
		cursor.Decode(&province)
		allProvince = append(allProvince, province)
	}
	c.JSON(http.StatusOK, gin.H{
		"status": http.StatusOK,
		"data":   allProvince,
	})
	return
}

func main() {
	// Init Router
	router := gin.Default()

	router.GET("/hospitals", GetAllHospitals)
	router.GET("/hospitals/:id", GetHospitalByProvince)
	router.GET("/provinces", GetProvinces)

	log.Fatal(router.Run(":4747"))
}
