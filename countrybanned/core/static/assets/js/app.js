var country_demo = new Vue({
    el: '#country-demo',
    data: {
        countriesList: [],
        filterCountriesList: {},
        countryShow: true,
        countryFilterShow: false,
        successMesssage: false,
        countries: [
            {"name": "Afghanistan", "index": "A"}, {"name": "Australia", "index": "A"}, {"name": "Austria", "index": "A"},
            {"name": "Bangladesh", "index": "B"}, {"name": "Burkina Faso", "index": "B"}, {"name": "Burundi", "index": "B"},
            {"name": "Canada", "index": "C"}, {"name": "Cyprus", "index": "C"}, {"name": "Czech Republic", "index": "C"},
            {"name": "Denmark", "index": "D"}, {"name": "Djibouti", "index": "D"}, {"name": "Dominica", "index": "D"},
            {"name": "Ecuador", "index": "E"}, {"name": "Egypt", "index": "E"}, {"name": "El Salvador", "index": "E"},
            {"name": "Falkland Islands (Malvinas)", "index": "F"}, {"name": "Faroe Islands", "index": "F"}, {"name": "Fiji", "index": "F"},
            {"name": "Gabon", "index": "G"}, {"name": "Gambia", "index": "G"}, {"name": "Georgia", "index": "G"},
            {"name": "Haiti", "index": "H"}, {"name": "Heard Island and Mcdonald Islands", "index": "H"}, {"name": "Holy See (Vatican City State)", "index": "H"},
            {"name": "Iceland", "index": "I"}, {"name": "India", "index": "I"}, {"name": "Indonesia", "index": "I"},
            {"name": "Jamaica", "index": "J"}, {"name": "Japan", "index": "J"}, {"name": "Jersey", "index": "J"},
            {"name": "Kazakhstan", "index": "K"}, {"name": "Kenya", "index": "K"}, {"name": "Kiribati", "index": "K"},
            {"name": "Lao PeopleS Democratic Republic", "index": "L"}, {"name": "Latvia", "index": "L"}, {"name": "Lebanon", "index": "L"},
            {"name": "Macao", "index": "M"}, {"name": "Macedonia, The Former Yugoslav Republic of", "index": "M"}, {"name": "Madagascar", "index": "M"},
            {"name": "Namibia", "index": "N"}, {"name": "Nauru", "index": "N"}, {"name": "Nepal", "index": "N"},
            {"name": "Oman", "index": "O"},
            {"name": "Pakistan", "index": "P"}, {"name": "Palau", "index": "P"}, {"name": "Palestinian Territory, Occupied", "index": "P"},
            {"name": "Qatar", "index": "Q"},
            {"name": "Reunion", "index": "R"}, {"name": "Romania", "index": "R"}, {"name": "Russian Federation", "index": "R"},
            {"name": "Saint Helena", "index": "S"}, {"name": "Saint Kitts and Nevis", "index": "S"}, {"name": "Saint Lucia", "index": "S"},
            {"name": "Taiwan, Province of China", "index": "T"}, {"name": "Tajikistan", "index": "T"}, {"name": "Tanzania, United Republic of", "index": "T"},
            {"name": "Uganda", "index": "U"}, {"name": "Ukraine", "index": "U"}, {"name": "United Arab Emirates", "index": "U"},
            {"name": "Vanuatu", "index": "V"}, {"name": "Venezuela", "index": "V"}, {"name": "Viet Nam", "index": "V"},
            {"name": "Wallis and Futuna", "index": "W"}, {"name": "Western Sahara", "index": "W"},
            {"name": "Yemen", "index": "Y"},
            {"name": "Zambia", "index": "Z"}, {"name": "Zimbabwe", "index": "Z"}
        ],
        filters: ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"],
    },
    beforeMount() {
        alert('hi');
        var countriesComputedStorage = localStorage.getItem("countriesComputed");
        if (countriesComputedStorage) {
            this.countriesList = JSON.parse(countriesComputedStorage);
        }
    },
    computed: {
        countriesComputed() {
            return this.countriesList;
        }
    },
    methods: {
        filterCountries(filter) {
            this.filterCountriesList = {};
            this.filterCountriesList[filter.charAt(0)] = this.countries.filter( country => (country.index == filter.charAt(0)) );
            this.filterCountriesList[filter.charAt(1)] = this.countries.filter( country => (country.index == filter.charAt(1)) );
            this.filterCountriesList[filter.charAt(2)] = this.countries.filter( country => (country.index == filter.charAt(2)) );
            this.countryShow = false;
            this.countryFilterShow = true;
        },
        selectAllContries($event) {
            const checked = $event.target.checked;
            var selected = [];
            if (checked) {
                this.countries.forEach(function (country) {
                    selected.push(country.name);
                });
            }
            this.countriesList = selected;
        },
        saveSelectedCountries() {
            localStorage.setItem("countriesComputed", JSON.stringify(this.countriesList));
            this.successMesssage = true;

        },
        clearSelectedCountries() {
            localStorage.removeItem("countriesComputed");
            this.countriesList = [];
        },
    }
})
