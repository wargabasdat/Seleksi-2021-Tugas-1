package main

import (
	"context"
	"log"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	guuid "github.com/google/uuid"
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

func CreateHospital(c *gin.Context) {
	id := guuid.New().String()
	var hospital Hospital
	newUpdatedAt := UpdatedAt{
		Hour:   0,
		Minute: 0,
	}
	c.BindJSON(&hospital)
	name := hospital.Name
	address := hospital.Address
	bedAvailable := hospital.BedAvailable
	queue := hospital.Queue
	hotline := hospital.Hotline
	links := hospital.Details
	provinceId := hospital.ProvinceId
	newHospital := Hospital{
		ID:           id,
		Name:         name,
		Address:      address,
		BedAvailable: bedAvailable,
		Queue:        queue,
		Hotline:      hotline,
		UpdatedAt:    newUpdatedAt,
		Details:      links,
		ProvinceId:   provinceId,
	}
	collection, _ := getMongoDbCollection(dbName, collectionName)
	_, err := collection.InsertOne(context.TODO(), newHospital)
	if err != nil {
		log.Printf("Error while inserting new todo into db, Reason: %v\n", err)
		c.JSON(http.StatusInternalServerError, gin.H{
			"status":  http.StatusInternalServerError,
			"message": "Something went wrong",
		})
		return
	}
	c.JSON(http.StatusCreated, gin.H{
		"status":  http.StatusCreated,
		"message": "Hospital created Successfully",
		"newId":   id,
	})
	return
}
func GetSingleHospital(c *gin.Context) {
	id := c.Param("id")
	hospital := Hospital{}
	collection, _ := getMongoDbCollection(dbName, collectionName)
	err := collection.FindOne(context.TODO(), bson.M{"id": id}).Decode(&hospital)
	if err != nil {
		log.Printf("Error while getting a single hospital, Reason: %v\n", err)
		c.JSON(http.StatusNotFound, gin.H{
			"status":  http.StatusNotFound,
			"message": "Hospital not found",
		})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"status":  http.StatusOK,
		"message": "Data delivered successfully",
		"data":    hospital,
	})
	return
}

func UpdateHospital(c *gin.Context) {
	id := c.Param("id")
	hospital := Hospital{}
	collection, _ := getMongoDbCollection(dbName, collectionName)
	err := collection.FindOne(context.TODO(), bson.M{"id": id}).Decode(&hospital)
	if err != nil {
		log.Printf("Error while getting a single hospital, Reason: %v\n", err)
		c.JSON(http.StatusNotFound, gin.H{
			"status":  http.StatusNotFound,
			"message": "Hospital not found",
		})
		return
	}
	var newHospital Hospital
	c.BindJSON(&newHospital)
	name := newHospital.Name
	if name == "" {
		name = hospital.Name
	}
	address := newHospital.Address
	if address == "" {
		address = hospital.Address
	}
	bedAvailable := newHospital.BedAvailable
	if bedAvailable == 0 {
		bedAvailable = hospital.BedAvailable
	}
	queue := newHospital.Queue
	if queue == 0 {
		queue = hospital.Queue
	}
	hotline := newHospital.Hotline
	if hotline == "" {
		hotline = hospital.Hotline
	}
	links := newHospital.Details
	if links == "" {
		links = hospital.Details
	}
	provinceId := newHospital.ProvinceId
	if provinceId == 0 {
		provinceId = hospital.ProvinceId
	}
	newData := bson.M{
		"$set": bson.M{
			"name":         name,
			"address":      address,
			"bedAvailable": bedAvailable,
			"queue":        queue,
			"hotline":      hotline,
			"links":        links,
			"provinceId":   provinceId,
		},
	}
	data, err := collection.UpdateOne(context.TODO(), bson.M{"id": id}, newData)
	if err != nil {
		log.Printf("Error, Reason: %v\n", err)
		c.JSON(http.StatusInternalServerError, gin.H{
			"status":  500,
			"message": "Something went wrong",
			"data":    data,
		})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"status":  200,
		"message": "Hospital Updated Successfully",
	})
	return
}

func DeleteHospital(c *gin.Context) {
	id := c.Param("id")
	collection, _ := getMongoDbCollection(dbName, collectionName)
	_, err := collection.DeleteOne(context.TODO(), bson.M{"id": id})
	if err != nil {
		log.Printf("Error while deleting a single hospital, Reason: %v\n", err)
		c.JSON(http.StatusInternalServerError, gin.H{
			"status":  http.StatusInternalServerError,
			"message": "Something went wrong",
		})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"status":  http.StatusOK,
		"message": "Hospital deleted successfully",
	})
	return
}

func main() {
	// Init Router
	router := gin.Default()

	router.GET("/hospital", GetAllHospitals)
	router.GET("/hospital/:id", GetSingleHospital)
	router.PATCH("/hospital/:id", UpdateHospital)
	router.DELETE("/hospital/:id", DeleteHospital)
	router.POST("/hospital", CreateHospital)
	router.GET("/province/:id", GetHospitalByProvince)
	router.GET("/province", GetProvinces)

	log.Fatal(router.Run(":4747"))
}
