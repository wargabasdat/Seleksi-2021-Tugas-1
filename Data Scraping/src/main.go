package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"regexp"
	"strconv"

	"github.com/gocolly/colly"
	guuid "github.com/google/uuid"
)

var provinceID = [34]int{11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 31, 32, 33, 34, 35, 36, 51, 52, 53, 61, 62, 63, 64, 65, 71, 72, 73, 74, 75, 76, 81, 82, 91, 94}

var MapProvinceID = map[int]string{
	11: "ACEH",
	12: "SUMATERA UTARA",
	13: "SUMATERA BARAT",
	14: "RIAU",
	15: "JAMBI",
	16: "SUMATERA SELATAN",
	17: "BENGKULU",
	18: "LAMPUNG",
	19: "KEPULAUAN BANGKA BELITUNG",
	21: "KEPULAUAN RIAU",
	31: "DKI JAKARTA",
	32: "JAWA BARAT",
	33: "JAWA TENGAH",
	34: "DI YOGYAKARTA",
	35: "JAWA TIMUR",
	36: "BANTEN",
	51: "BALI",
	52: "NUSA TENGGARA BARAT",
	53: "NUSA TENGGARA TIMUR",
	61: "KALIMANTAN BARAT",
	62: "KALIMANTAN TENGAH",
	63: "KALIMANTAN SELATAN",
	64: "KALIMANTAN TIMUR",
	65: "KALIMANTAN UTARA",
	71: "SULAWESI UTARA",
	72: "SULAWESI TENGAH",
	73: "SULAWESI SELATAN",
	74: "SULAWESI TENGGARA",
	75: "GORONTALO",
	76: "SULAWESI BARAT",
	81: "MALUKU",
	82: "MALUKU UTARA",
	91: "PAPUA BARAT",
	94: "PAPUA",
}

type Province struct {
	ID   int    `json:"provinceId"`
	Name string `json:"name"`
}

type UpdatedAt struct {
	Hour   int `json:"hour"`
	Minute int `json:"minute"`
}

type Hospital struct {
	ID           string    `json:"id"`
	Name         string    `json:"name"`
	Address      string    `json:"address"`
	BedAvailable int       `json:"bedAvailable"`
	Queue        int       `json:"queue"`
	Hotline      string    `json:"hotline"`
	UpdatedAt    UpdatedAt `json:"updatedAt"`
	Details      string    `json:"links"`
	ProvinceId   int       `json:"provinceId"`
}

func main() {
	var regex, _ = regexp.Compile(`[0-9]+`)
	var minute, _ = regexp.Compile(`menit`)
	var hour, _ = regexp.Compile(`jam`)
	allHospital := make([]Hospital, 0)
	allProvince := make([]Province, 0)

	//Inisiasi Colly untuk scrapping dengan domain yang digunakan
	collector := colly.NewCollector(colly.AllowedDomains("yankes.kemkes.go.id", "www.yankes.kemkes.go.id"))
	for i := 0; i < len(provinceID); i++ {
		//Mencari element dengan class card
		collector.OnHTML(".card", func(element *colly.HTMLElement) {
			//Data adding Menggunakan UUID sehingga id unique
			id := guuid.New().String()
			//ChildText digunakan untuk mendapat text html dengan param query selector
			name := element.ChildText("h5")
			address := element.ChildText("div.col-md-7 p.mb-0")
			//Data Transformation fungsi Atoi digunakan untuk convert string to int
			bed, _ := strconv.Atoi(element.ChildText("div.col-md-5.text-right p.mb-0 b"))
			//Data Transformation fungsi Atoi digunakan untuk convert string to int
			hotline := element.ChildText("span")
			queue, _ := strconv.Atoi(regex.FindString(element.ChildText("div.card-body div.row div.col-md-5.text-right p.mb-0:nth-of-type(3)")))

			details := element.ChildAttr("a[href]", "href")

			hours := 0
			minutes := 0
			if minute.FindString(element.ChildText("div.card-body div.row div.col-md-5.text-right p.mb-0:nth-of-type(4)")) != "" {
				//data parsing untuk mendapat menit
				minutes, _ = strconv.Atoi(regex.FindString(element.ChildText("div.card-body div.row div.col-md-5.text-right p.mb-0:nth-of-type(4)")))
			}
			if hour.FindString(element.ChildText("div.card-body div.row div.col-md-5.text-right p.mb-0:nth-of-type(4)")) != "" {
				//data parsing untuk mendapat jam
				hours, _ = strconv.Atoi(regex.FindString(element.ChildText("div.card-body div.row div.col-md-5.text-right p.mb-0:nth-of-type(4)")))
			}

			updated := UpdatedAt{
				Hour:   hours,
				Minute: minutes,
			}

			hospital := Hospital{
				ID:           id,
				Name:         name,
				Address:      address,
				BedAvailable: bed,
				Hotline:      hotline,
				ProvinceId:   provinceID[i],
				Details:      details,
				Queue:        queue,
				UpdatedAt:    updated,
			}

			allHospital = append(allHospital, hospital)

		})
		// fungsi untuk membuat colly melakukan parsing
		collector.OnRequest(func(r *colly.Request) {
			fmt.Println("Visiting: ", r.URL.String())
		})
		// fungsi untuk membuat colly melakukan visit ke halaman web
		collector.Visit(fmt.Sprintf("http://yankes.kemkes.go.id/app/siranap/rumah_sakit?jenis=1&propinsi=%dprop&kabkota", provinceID[i]))

		province := Province{
			ID:   provinceID[i],
			Name: MapProvinceID[provinceID[i]],
		}

		allProvince = append(allProvince, province)
	}

	//Pada Web Scraping ini saya menggunakan Struct dalam scrapping karena lebih pasti angkanya tepat dibandingkan membuat array kemudian disatukan

	//Memprint json ke terminal
	enc := json.NewEncoder(os.Stdout)
	enc.SetEscapeHTML(false)
	enc.SetIndent("", " ")
	enc.Encode(allHospital)

	writeJSONHospital(allHospital)
	writeJSONProvince(allProvince)

}

//membuat file hospital.json
func writeJSONHospital(data []Hospital) {
	file, err := MarshalIndent(data, "", " ")
	if err != nil {
		log.Println("Unable to create a JSON file")
		return
	}
	_ = ioutil.WriteFile("hospital.json", file, 0644)
}

//membuat file province.json
func writeJSONProvince(data []Province) {
	file, err := json.MarshalIndent(data, "", " ")
	if err != nil {
		log.Println("Unable to create a JSON file")
		return
	}
	_ = ioutil.WriteFile("province.json", file, 0644)
}

//fungsi membuat json Bytes
func JSONMarshal(t interface{}) ([]byte, error) {
	buffer := &bytes.Buffer{}
	encoder := json.NewEncoder(buffer)
	encoder.SetEscapeHTML(false)
	err := encoder.Encode(t)
	return buffer.Bytes(), err
}

//fungsi membuat json Bytes memiliki indentasi
func MarshalIndent(v interface{}, prefix, indent string) ([]byte, error) {
	b, err := JSONMarshal(v)
	if err != nil {
		return nil, err
	}
	var buf bytes.Buffer
	err = json.Indent(&buf, b, prefix, indent)
	if err != nil {
		return nil, err
	}
	return buf.Bytes(), nil
}
