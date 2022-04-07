
<!-- PROJECT LOGO -->
<br />
<div align="center">
 

  <h1 align="center">Import Stocks to mysql from thinkorswim api</h1>

</div>



<!-- ABOUT THE PROJECT -->
## About The Project


This program requests data from the thinkorswim api and imports the data to mysql.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* pandas
  ```sh
  $ python -m pip install pandas
  ```

* requests
  ```sh
  $ python -m pip install requests
  ```

* pymysql
  ```sh
  $ pip install mysql
  ```
### Installation

_Below is an example of how to get started with the program._
1. Get a free API Key at [https://developer.tdameritrade.com/apis]
2. Clone the repo
   ```sh
   git clone https://github.com/jym06298/import_stock.git
   ```
3. Enter your API in as an environment variable
   ```sh
   $ export API_KEY='YOUR API KEY'
   ``` 
   

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* import data to csv files from thinkorswim api. 
  ```sh
  $ python import_stock_csv.py
* import data to mysql from csv files. 
  ```sh
  $ python db_stock.py
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jun Mun - jym06298@uga.edu

Project Link: [https://github.com/jym06298/import_stocks](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>





