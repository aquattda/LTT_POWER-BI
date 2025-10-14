**POWER BI – DAY 1**

**Overview of PBI**

**Important concepts:**

- Methods that can getData in PBI: Methods that can getData in PBI:

+ File CSV/XLSX…

+ Scrape data about the website (Can learn)

+ Get data from the API (Can learn)

- ETL (EXTRACT, TRANSFORM, LOAD) is a process used in data warehousing and data integration. Extract data from various (/ˈver.i.əs/: đa dạng) sources (<sɔːrs/>), transforming it into a suitable (phù hợp) format, and loading it into a target database or data warehouse. This process helps in consolidating (consolidate /kənˈsɑː.lə.deɪt/: Hợp nhất) data for analysis and reporting purposes. (purpose /ˈpɝː.pəs/ = aim = target: Mục đích)

POWER BI – DAY 2

CLEAN DATA

Important concepts:

- Before cleaning data, you need to adjust some things:

<<<<<<<<<<<<<IMAGE>>>>>>>>>>>>>>>>>>>>>>>>>
- Differences when using Filter with EXCEL and PBI:

+ Excel: After using the filter, the filtered data will disappear /ˌdɪs.əˈpɪr/ (Be gone: Mất tiêu lun).

+ PBI: After using the filter, the filltered data will be hidden Sau khi sử dụng Filter thì dữ liệu chỉ bị ẩn đi

POWER BI – DAY 3

DATA MODEL (Star schema)

Important concepts:

- Relationship and Keys (Primary Key and Foreign Key)

+ Normally, table has a single primary key, but it's also possible to have more than one (Uncommon).

+ UUID (Universally unique identifier /aɪˈdentɪfaɪər/) (128-bit) provides a huge range (Almost infinite /ˈɪn.fə.nət/ range), while INT (32-bit) supports values (~ 2 bilion)

+ In this data model, 'Data' is the Fact table, and 'Lookup' is the Dimension table.

<<<<<<<<<<<<<IMAGE>>>>>>>>>>>>>>>>>>>>>>>>>


- Here’s the structure: Fact_Survey is our Fact table, and Dim_AgeGroup and Dim_Location are Dimension tables used for lookups.
