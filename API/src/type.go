package main

type Province struct {
	ID   int    `bson:"provinceId"`
	Name string `bson:"name"`
}

type UpdatedAt struct {
	Hour   int `bson:"hour"`
	Minute int `bson:"minute"`
}

type Hospital struct {
	Name         string    `bson:"name"`
	Address      string    `bson:"address"`
	BedAvailable int       `bson:"bedAvailable"`
	Queue        int       `bson:"queue"`
	Hotline      string    `bson:"hotline"`
	UpdatedAt    UpdatedAt `bson:"updatedAt"`
	Details      string    `bson:"links"`
	ProvinceId   int       `bson:"provinceId"`
}
