# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
import re
import urllib2
from datetime import datetime, timedelta
from scrapy import log, Request
from yg.items import YgItem
from scrapy.spider import Spider
import unicodedata

class LhmartSpider(Spider):
    name = "lhmart"
    allowed_domains = ["lhmart.com"]
    start_urls = [

"http://www.lhmart.com/catalog/s-29-39-62",
"http://www.lhmart.com/catalog/s-29-39-63",
"http://www.lhmart.com/catalog/s-29-39-64",
"http://www.lhmart.com/catalog/s-29-39-66",
"http://www.lhmart.com/catalog/s-29-39-65",

"http://www.lhmart.com/catalog/s-29-38-55",
"http://www.lhmart.com/catalog/s-29-38-54",
"http://www.lhmart.com/catalog/s-29-38-56",
"http://www.lhmart.com/catalog/s-29-38-59",
"http://www.lhmart.com/catalog/s-29-38-57",
"http://www.lhmart.com/catalog/s-29-38-58",
"http://www.lhmart.com/catalog/s-29-38-60",
"http://www.lhmart.com/catalog/s-29-38-61",
"http://www.lhmart.com/catalog/s-29-40",
"http://www.lhmart.com/catalog/s-29-40-74",
"http://www.lhmart.com/catalog/s-29-40-68",
"http://www.lhmart.com/catalog/s-29-40-69",
"http://www.lhmart.com/catalog/s-29-40-70",
"http://www.lhmart.com/catalog/s-29-40-71",
"http://www.lhmart.com/catalog/s-29-40-72",
"http://www.lhmart.com/catalog/s-29-40-73",
"http://www.lhmart.com/catalog/s-29-40-75",
"http://www.lhmart.com/catalog/s-29-40-77",
"http://www.lhmart.com/catalog/s-29-40-578",
"http://www.lhmart.com/catalog/s-29-40-76",
"http://www.lhmart.com/catalog/s-29-41-78",

"http://www.lhmart.com/catalog/s-29-41-79",
"http://www.lhmart.com/catalog/s-29-41-80",
"http://www.lhmart.com/catalog/s-29-41-81",
"http://www.lhmart.com/catalog/s-29-41-82",
#beverage
"http://www.lhmart.com/catalog/s-29-42",
"http://www.lhmart.com/catalog/s-29-42-83",
"http://www.lhmart.com/catalog/s-29-42-84",
"http://www.lhmart.com/catalog/s-29-42-85",
"http://www.lhmart.com/catalog/s-29-42-86",
"http://www.lhmart.com/catalog/s-29-42-87",
"http://www.lhmart.com/catalog/s-29-42-88",
"http://www.lhmart.com/catalog/s-29-42-89",
# alchohol
"http://www.lhmart.com/catalog/s-29-43",
"http://www.lhmart.com/catalog/s-29-43-90",
"http://www.lhmart.com/catalog/s-29-43-91",
"http://www.lhmart.com/catalog/s-29-43-92",
"http://www.lhmart.com/catalog/s-29-43-93",
"http://www.lhmart.com/catalog/s-29-43-94",
"http://www.lhmart.com/catalog/s-29-43-95",
"http://www.lhmart.com/catalog/s-29-43-96",
"http://www.lhmart.com/catalog/s-29-43-97",
"http://www.lhmart.com/catalog/s-29-43-1707",

# coffee and tea
"http://www.lhmart.com/catalog/s-29-44",
"http://www.lhmart.com/catalog/s-29-44-98",
"http://www.lhmart.com/catalog/s-29-44-1522",
"http://www.lhmart.com/catalog/s-29-44-99",
"http://www.lhmart.com/catalog/s-29-44-100",
"http://www.lhmart.com/catalog/s-29-44-101",

"http://www.lhmart.com/catalog/s-29-45",
"http://www.lhmart.com/catalog/s-29-45-102",
"http://www.lhmart.com/catalog/s-29-45-103",
"http://www.lhmart.com/catalog/s-29-45-104",
"http://www.lhmart.com/catalog/s-29-45-105",
"http://www.lhmart.com/catalog/s-29-45-106",
"http://www.lhmart.com/catalog/s-29-45-107",

"http://www.lhmart.com/catalog/s-29-46",
"http://www.lhmart.com/catalog/s-29-46-109",
"http://www.lhmart.com/catalog/s-29-46-110",

"http://www.lhmart.com/catalog/s-29-47",
"http://www.lhmart.com/catalog/s-29-47-111",
"http://www.lhmart.com/catalog/s-29-47-112",
"http://www.lhmart.com/catalog/s-29-47-113",
"http://www.lhmart.com/catalog/s-29-47-114",
"http://www.lhmart.com/catalog/s-29-47-116",
"http://www.lhmart.com/catalog/s-29-47-117",
"http://www.lhmart.com/catalog/s-29-47-580",
"http://www.lhmart.com/catalog/s-29-47-115",
"http://www.lhmart.com/catalog/s-29-47-579",

"http://www.lhmart.com/catalog/s-29-48",
"http://www.lhmart.com/catalog/s-29-48-118",
"http://www.lhmart.com/catalog/s-29-48-119",

"http://www.lhmart.com/catalog/s-29-49",
"http://www.lhmart.com/catalog/s-29-49-121",
"http://www.lhmart.com/catalog/s-29-49-122",
"http://www.lhmart.com/catalog/s-29-49-123",
"http://www.lhmart.com/catalog/s-29-49-124",
"http://www.lhmart.com/catalog/s-29-49-125",

"http://www.lhmart.com/catalog/s-29-50",
"http://www.lhmart.com/catalog/s-29-50-126",
"http://www.lhmart.com/catalog/s-29-50-1113",
"http://www.lhmart.com/catalog/s-29-50-127",
"http://www.lhmart.com/catalog/s-29-50-128",
"http://www.lhmart.com/catalog/s-29-50-129",
"http://www.lhmart.com/catalog/s-29-50-130",
"http://www.lhmart.com/catalog/s-29-50-131",

"http://www.lhmart.com/catalog/s-29-51",
"http://www.lhmart.com/catalog/s-29-51-132",
"http://www.lhmart.com/catalog/s-29-51-1108",
"http://www.lhmart.com/catalog/s-29-51-133",
"http://www.lhmart.com/catalog/s-29-51-134",
"http://www.lhmart.com/catalog/s-29-51-135",

"http://www.lhmart.com/catalog/s-29-52",
"http://www.lhmart.com/catalog/s-29-52-136",
"http://www.lhmart.com/catalog/s-29-52-137",
"http://www.lhmart.com/catalog/s-29-52-139",
"http://www.lhmart.com/catalog/s-29-52-140",

"http://www.lhmart.com/catalog/s-29-53",
"http://www.lhmart.com/catalog/s-29-53-142",
"http://www.lhmart.com/catalog/s-29-53-141",
"http://www.lhmart.com/catalog/s-29-53-143",
"http://www.lhmart.com/catalog/s-29-53-144",

#VEGETABLES
"http://www.lhmart.com/catalog/s-920-934",
"http://www.lhmart.com/catalog/s-920-934-991",
"http://www.lhmart.com/catalog/s-920-934-946",
"http://www.lhmart.com/catalog/s-920-934-951",
"http://www.lhmart.com/catalog/s-920-934-938",

"http://www.lhmart.com/catalog/s-920-931",
"http://www.lhmart.com/catalog/s-920-931-1148",
"http://www.lhmart.com/catalog/s-920-931-932",

"http://www.lhmart.com/catalog/s-920-935",
"http://www.lhmart.com/catalog/s-920-935-944",
"http://www.lhmart.com/catalog/s-920-935-964",
"http://www.lhmart.com/catalog/s-920-935-965",
"http://www.lhmart.com/catalog/s-920-935-985",

"http://www.lhmart.com/catalog/s-920-947",
"http://www.lhmart.com/catalog/s-920-947-949",
"http://www.lhmart.com/catalog/s-920-947-1029",
"http://www.lhmart.com/catalog/s-920-947-1035",
"http://www.lhmart.com/catalog/s-920-947-1587",
"http://www.lhmart.com/catalog/s-920-947-1154",
"http://www.lhmart.com/catalog/s-920-947-987",
"http://www.lhmart.com/catalog/s-920-947-1026",

"http://www.lhmart.com/catalog/s-920-948",
"http://www.lhmart.com/catalog/s-920-948-1037",
"http://www.lhmart.com/catalog/s-920-948-954",
"http://www.lhmart.com/catalog/s-920-948-1523",
"http://www.lhmart.com/catalog/s-920-948-953",
"http://www.lhmart.com/catalog/s-920-948-1038",

"http://www.lhmart.com/catalog/s-920-980",
"http://www.lhmart.com/catalog/s-920-980-981",
"http://www.lhmart.com/catalog/s-920-980-983",
"http://www.lhmart.com/catalog/s-920-980-1024",
"http://www.lhmart.com/catalog/s-920-980-984",
"http://www.lhmart.com/catalog/s-920-980-982",
"http://www.lhmart.com/catalog/s-920-980-1025",


"http://www.lhmart.com/catalog/s-920-1009",
"http://www.lhmart.com/catalog/s-920-1009-1010",
"http://www.lhmart.com/catalog/s-920-1009-1011",
"http://www.lhmart.com/catalog/s-920-1009-1124",
"http://www.lhmart.com/catalog/s-920-1009-1023",



"http://www.lhmart.com/catalog/s-920-1017",
"http://www.lhmart.com/catalog/s-920-1017-1018",
"http://www.lhmart.com/catalog/s-920-1017-1039",
"http://www.lhmart.com/catalog/s-920-1017-1524",
"http://www.lhmart.com/catalog/s-920-1017-1155",
"http://www.lhmart.com/catalog/s-920-1017-1041",
"http://www.lhmart.com/catalog/s-920-1017-1495",

"http://www.lhmart.com/catalog/s-920-1040",
"http://www.lhmart.com/catalog/s-920-1040-1118",
"http://www.lhmart.com/catalog/s-920-1040-1042",
"http://www.lhmart.com/catalog/s-920-1040-1119",

# baby mother 10 sub_cate
"http://www.lhmart.com/catalog/p-30",
"http://www.lhmart.com/catalog/s-30-145",
"http://www.lhmart.com/catalog/s-30-145-1064",
"http://www.lhmart.com/catalog/s-30-145-1065",
"http://www.lhmart.com/catalog/s-30-145-1066",
"http://www.lhmart.com/catalog/s-30-145-1067",
"http://www.lhmart.com/catalog/s-30-145-890",

"http://www.lhmart.com/catalog/s-30-148",
"http://www.lhmart.com/catalog/s-30-148-1075",
"http://www.lhmart.com/catalog/s-30-148-1076",
"http://www.lhmart.com/catalog/s-30-148-1077",
"http://www.lhmart.com/catalog/s-30-148-1078",
"http://www.lhmart.com/catalog/s-30-148-1079",
"http://www.lhmart.com/catalog/s-30-148-1080",
"http://www.lhmart.com/catalog/s-30-148-1081",

"http://www.lhmart.com/catalog/s-30-1089",
"http://www.lhmart.com/catalog/s-30-1089-1090",
"http://www.lhmart.com/catalog/s-30-1089-1091",
"http://www.lhmart.com/catalog/s-30-1089-1092",
"http://www.lhmart.com/catalog/s-30-1089-1093",

"http://www.lhmart.com/catalog/s-30-146",
"http://www.lhmart.com/catalog/s-30-146-198",
"http://www.lhmart.com/catalog/s-30-146-1068",
"http://www.lhmart.com/catalog/s-30-146-1069",
"http://www.lhmart.com/catalog/s-30-146-203",
"http://www.lhmart.com/catalog/s-30-146-204",

"http://www.lhmart.com/catalog/s-30-149",
"http://www.lhmart.com/catalog/s-30-149-1088",
"http://www.lhmart.com/catalog/s-30-149-1082",
"http://www.lhmart.com/catalog/s-30-149-1087",
"http://www.lhmart.com/catalog/s-30-149-1084",
"http://www.lhmart.com/catalog/s-30-149-1083",
"http://www.lhmart.com/catalog/s-30-149-1086",
"http://www.lhmart.com/catalog/s-30-149-1085",

"http://www.lhmart.com/catalog/s-30-481",
"http://www.lhmart.com/catalog/s-30-481-482",
"http://www.lhmart.com/catalog/s-30-481-486",
"http://www.lhmart.com/catalog/s-30-481-489",
"http://www.lhmart.com/catalog/s-30-481-496",
"http://www.lhmart.com/catalog/s-30-481-500",
"http://www.lhmart.com/catalog/s-30-481-502",
"http://www.lhmart.com/catalog/s-30-481-507",
"http://www.lhmart.com/catalog/s-30-481-509",
"http://www.lhmart.com/catalog/s-30-481-513",
"http://www.lhmart.com/catalog/s-30-481-514",
"http://www.lhmart.com/catalog/s-30-481-518",
"http://www.lhmart.com/catalog/s-30-481-521",


"http://www.lhmart.com/catalog/s-30-1057",
"http://www.lhmart.com/catalog/s-30-1057-1061",
"http://www.lhmart.com/catalog/s-30-1057-1060",
"http://www.lhmart.com/catalog/s-30-1057-1059",



"http://www.lhmart.com/catalog/s-30-1095",
"http://www.lhmart.com/catalog/s-30-1095-1096",
"http://www.lhmart.com/catalog/s-30-1095-1097",
"http://www.lhmart.com/catalog/s-30-1095-1106",
"http://www.lhmart.com/catalog/s-30-1095-1099",
"http://www.lhmart.com/catalog/s-30-1095-1101",
"http://www.lhmart.com/catalog/s-30-1095-1103",

# beauty and health cosmic in total 6
#1
"http://www.lhmart.com/catalog/s-31-994",
"http://www.lhmart.com/catalog/s-31-994-1498",
"http://www.lhmart.com/catalog/s-31-994-1499",
"http://www.lhmart.com/catalog/s-31-994-997",
"http://www.lhmart.com/catalog/s-31-994-1109",
"http://www.lhmart.com/catalog/s-31-994-996",
"http://www.lhmart.com/catalog/s-31-994-1056",
"http://www.lhmart.com/catalog/s-31-994-1107",
"http://www.lhmart.com/catalog/s-31-994-1005",
"http://www.lhmart.com/catalog/s-31-994-998",
#2
"http://www.lhmart.com/catalog/s-31-215",
"http://www.lhmart.com/catalog/s-31-215-1044",
"http://www.lhmart.com/catalog/s-31-215-270",
"http://www.lhmart.com/catalog/s-31-215-272",
"http://www.lhmart.com/catalog/s-31-215-275",
"http://www.lhmart.com/catalog/s-31-215-273",
"http://www.lhmart.com/catalog/s-31-215-274",
"http://www.lhmart.com/catalog/s-31-215-276",
#3
"http://www.lhmart.com/catalog/s-31-216",
"http://www.lhmart.com/catalog/s-31-216-265",
"http://www.lhmart.com/catalog/s-31-216-266",
"http://www.lhmart.com/catalog/s-31-216-268",
"http://www.lhmart.com/catalog/s-31-216-267",
#4
"http://www.lhmart.com/catalog/s-31-217-260",
"http://www.lhmart.com/catalog/s-31-217-258",
"http://www.lhmart.com/catalog/s-31-217-261",
"http://www.lhmart.com/catalog/s-31-217-263",
"http://www.lhmart.com/catalog/s-31-217-262",
"http://www.lhmart.com/catalog/s-31-217-264",
#5
"http://www.lhmart.com/catalog/s-31-219",
#6
"http://www.lhmart.com/catalog/s-31-220",
"http://www.lhmart.com/catalog/s-31-220-247",
"http://www.lhmart.com/catalog/s-31-220-248",
"http://www.lhmart.com/catalog/s-31-220-249",
"http://www.lhmart.com/catalog/s-31-220-250",

# personal care and cleaness 8
"http://www.lhmart.com/catalog/s-443-1110",
"http://www.lhmart.com/catalog/s-443-1110-1111",
"http://www.lhmart.com/catalog/s-443-1110-1112",
"http://www.lhmart.com/catalog/s-443-1110-1519",
"http://www.lhmart.com/catalog/s-443-1110-1520",
"http://www.lhmart.com/catalog/s-443-1110-1521",

"http://www.lhmart.com/catalog/s-443-444",
"http://www.lhmart.com/catalog/s-443-444-445",
"http://www.lhmart.com/catalog/s-443-444-1598",
"http://www.lhmart.com/catalog/s-443-444-446",

"http://www.lhmart.com/catalog/s-443-452",
"http://www.lhmart.com/catalog/s-443-452-457",
"http://www.lhmart.com/catalog/s-443-452-454",
"http://www.lhmart.com/catalog/s-443-452-455",
"http://www.lhmart.com/catalog/s-443-452-1595",
"http://www.lhmart.com/catalog/s-443-452-1596",

"http://www.lhmart.com/catalog/s-443-458",
"http://www.lhmart.com/catalog/s-443-458-459",
"http://www.lhmart.com/catalog/s-443-458-1597",
"http://www.lhmart.com/catalog/s-443-458-460",
"http://www.lhmart.com/catalog/s-443-458-461",


"http://www.lhmart.com/catalog/s-443-218",
"http://www.lhmart.com/catalog/s-443-218-255",
"http://www.lhmart.com/catalog/s-443-218-974",
"http://www.lhmart.com/catalog/s-443-218-256",
"http://www.lhmart.com/catalog/s-443-218-257",

"http://www.lhmart.com/catalog/s-443-449",
"http://www.lhmart.com/catalog/s-443-449-450",
"http://www.lhmart.com/catalog/s-443-449-451",

"http://www.lhmart.com/catalog/s-443-1046",
"http://www.lhmart.com/catalog/s-443-1046-1053",
"http://www.lhmart.com/catalog/s-443-1046-1054",
"http://www.lhmart.com/catalog/s-443-1046-1055",

"http://www.lhmart.com/catalog/s-443-1045",
"http://www.lhmart.com/catalog/s-443-1045-1047",
"http://www.lhmart.com/catalog/s-443-1045-1048",
"http://www.lhmart.com/catalog/s-443-1045-1049",
"http://www.lhmart.com/catalog/s-443-1045-1050",
"http://www.lhmart.com/catalog/s-443-1045-1051",
"http://www.lhmart.com/catalog/s-443-1045-1052",

# clean
"http://www.lhmart.com/catalog/s-33-316",
"http://www.lhmart.com/catalog/s-33-316-319",
"http://www.lhmart.com/catalog/s-33-316-1230",
"http://www.lhmart.com/catalog/s-33-316-320",
"http://www.lhmart.com/catalog/s-33-316-321",
"http://www.lhmart.com/catalog/s-33-316-322",
"http://www.lhmart.com/catalog/s-33-316-323",
"http://www.lhmart.com/catalog/s-33-316-324",

"http://www.lhmart.com/catalog/s-33-1244",
"http://www.lhmart.com/catalog/s-33-1244-1247",
"http://www.lhmart.com/catalog/s-33-1244-1248",
"http://www.lhmart.com/catalog/s-33-1244-1249",
"http://www.lhmart.com/catalog/s-33-1244-1250",
"http://www.lhmart.com/catalog/s-33-1244-1251",
"http://www.lhmart.com/catalog/s-33-1244-1252",
"http://www.lhmart.com/catalog/s-33-1244-1530",

"http://www.lhmart.com/catalog/s-33-1246",
"http://www.lhmart.com/catalog/s-33-1246-1259",
"http://www.lhmart.com/catalog/s-33-1246-1260",
"http://www.lhmart.com/catalog/s-33-1246-1261",
"http://www.lhmart.com/catalog/s-33-1246-1262",
"http://www.lhmart.com/catalog/s-33-1246-1263",
"http://www.lhmart.com/catalog/s-33-1246-1525",
"http://www.lhmart.com/catalog/s-33-1246-1526",
"http://www.lhmart.com/catalog/s-33-1246-1527",
"http://www.lhmart.com/catalog/s-33-1246-1528",
"http://www.lhmart.com/catalog/s-33-1246-1529",

"http://www.lhmart.com/catalog/s-33-318",
"http://www.lhmart.com/catalog/s-33-318-336",
"http://www.lhmart.com/catalog/s-33-318-337",
"http://www.lhmart.com/catalog/s-33-318-338",
"http://www.lhmart.com/catalog/s-33-318-339",

# kitchen utilities
"http://www.lhmart.com/catalog/s-34-341",
"http://www.lhmart.com/catalog/s-34-341-1585",
"http://www.lhmart.com/catalog/s-34-341-1272",
"http://www.lhmart.com/catalog/s-34-341-1275",
"http://www.lhmart.com/catalog/s-34-341-1273",
"http://www.lhmart.com/catalog/s-34-341-1276",
"http://www.lhmart.com/catalog/s-34-341-1274",
"http://www.lhmart.com/catalog/s-34-341-1277",
"http://www.lhmart.com/catalog/s-34-341-348",
"http://www.lhmart.com/catalog/s-34-341-347",
"http://www.lhmart.com/catalog/s-34-341-1584",

"http://www.lhmart.com/catalog/s-34-342",
"http://www.lhmart.com/catalog/s-34-342-1497",

"http://www.lhmart.com/catalog/s-34-342-357",
"http://www.lhmart.com/catalog/s-34-342-356",
"http://www.lhmart.com/catalog/s-34-342-358",

"http://www.lhmart.com/catalog/s-34-343",
"http://www.lhmart.com/catalog/s-34-343-362",
"http://www.lhmart.com/catalog/s-34-343-363",
"http://www.lhmart.com/catalog/s-34-343-359",
"http://www.lhmart.com/catalog/s-34-343-360",
"http://www.lhmart.com/catalog/s-34-343-361",

"http://www.lhmart.com/catalog/s-34-344",
"http://www.lhmart.com/catalog/s-34-344-364",
"http://www.lhmart.com/catalog/s-34-344-365",
"http://www.lhmart.com/catalog/s-34-344-366",

"http://www.lhmart.com/catalog/s-34-345",
"http://www.lhmart.com/catalog/s-34-345-349",
"http://www.lhmart.com/catalog/s-34-345-350",
"http://www.lhmart.com/catalog/s-34-345-351",
"http://www.lhmart.com/catalog/s-34-345-352",
"http://www.lhmart.com/catalog/s-34-345-353",
"http://www.lhmart.com/catalog/s-34-345-354",

# bathroom related
"http://www.lhmart.com/catalog/s-35-367",
"http://www.lhmart.com/catalog/s-35-367-374",
"http://www.lhmart.com/catalog/s-35-367-375",
"http://www.lhmart.com/catalog/s-35-367-376",
"http://www.lhmart.com/catalog/s-35-367-377",
"http://www.lhmart.com/catalog/s-35-367-378",
"http://www.lhmart.com/catalog/s-35-367-379",

"http://www.lhmart.com/catalog/s-35-958",
"http://www.lhmart.com/catalog/s-35-958-960",
"http://www.lhmart.com/catalog/s-35-958-961",
"http://www.lhmart.com/catalog/s-35-958-962",
"http://www.lhmart.com/catalog/s-35-958-963",

"http://www.lhmart.com/catalog/s-35-1030",
"http://www.lhmart.com/catalog/s-35-1030-1033",
"http://www.lhmart.com/catalog/s-35-1030-1034",

"http://www.lhmart.com/catalog/s-35-369-391",
"http://www.lhmart.com/catalog/s-35-369-384",
"http://www.lhmart.com/catalog/s-35-369-385",
"http://www.lhmart.com/catalog/s-35-369-386",
"http://www.lhmart.com/catalog/s-35-369-387",
"http://www.lhmart.com/catalog/s-35-369-388",
"http://www.lhmart.com/catalog/s-35-369-389",
"http://www.lhmart.com/catalog/s-35-369-390",
"http://www.lhmart.com/catalog/s-35-369-391",

"http://www.lhmart.com/catalog/s-35-371",
"http://www.lhmart.com/catalog/s-35-371-463",
"http://www.lhmart.com/catalog/s-35-371-464",

"http://www.lhmart.com/catalog/s-35-372",
"http://www.lhmart.com/catalog/s-35-372-401",

"http://www.lhmart.com/catalog/s-35-372-907",
"http://www.lhmart.com/catalog/s-35-372-957",
"http://www.lhmart.com/catalog/s-35-372-404",
"http://www.lhmart.com/catalog/s-35-372-403",
"http://www.lhmart.com/catalog/s-35-372-402",


"http://www.lhmart.com/catalog/s-35-373",
"http://www.lhmart.com/catalog/s-35-373-405",
"http://www.lhmart.com/catalog/s-35-373-406",
"http://www.lhmart.com/catalog/s-35-373-407",





"http://www.lhmart.com/catalog/s-35-368",
"http://www.lhmart.com/catalog/s-35-368-380",
"http://www.lhmart.com/catalog/s-35-368-381",
"http://www.lhmart.com/catalog/s-35-368-382",
"http://www.lhmart.com/catalog/s-35-368-383",

"http://www.lhmart.com/catalog/s-35-369",
"http://www.lhmart.com/catalog/s-35-369-384",
"http://www.lhmart.com/catalog/s-35-369-385",
"http://www.lhmart.com/catalog/s-35-369-386",
"http://www.lhmart.com/catalog/s-35-369-387",
"http://www.lhmart.com/catalog/s-35-369-388",
"http://www.lhmart.com/catalog/s-35-369-389",
"http://www.lhmart.com/catalog/s-35-369-390",
"http://www.lhmart.com/catalog/s-35-369-391",

# home electronic devices
"http://www.lhmart.com/catalog/s-37-169",
"http://www.lhmart.com/catalog/s-37-169-197",
"http://www.lhmart.com/catalog/s-37-169-193",
"http://www.lhmart.com/catalog/s-37-169-195",
"http://www.lhmart.com/catalog/s-37-169-1413",
"http://www.lhmart.com/catalog/s-37-169-196",

"http://www.lhmart.com/catalog/s-37-170",
"http://www.lhmart.com/catalog/s-37-170-223",
"http://www.lhmart.com/catalog/s-37-170-224",
"http://www.lhmart.com/catalog/s-37-170-228",
"http://www.lhmart.com/catalog/s-37-170-226",
"http://www.lhmart.com/catalog/s-37-170-225",
"http://www.lhmart.com/catalog/s-37-170-227",
"http://www.lhmart.com/catalog/s-37-170-1339",

"http://www.lhmart.com/catalog/s-37-171",
"http://www.lhmart.com/catalog/s-37-171-231",
"http://www.lhmart.com/catalog/s-37-171-1588",
"http://www.lhmart.com/catalog/s-37-171-232",
"http://www.lhmart.com/catalog/s-37-171-234",

"http://www.lhmart.com/catalog/s-37-172",
"http://www.lhmart.com/catalog/s-37-172-235",
"http://www.lhmart.com/catalog/s-37-172-1348",
"http://www.lhmart.com/catalog/s-37-172-1349",
"http://www.lhmart.com/catalog/s-37-172-236",
"http://www.lhmart.com/catalog/s-37-172-237",
"http://www.lhmart.com/catalog/s-37-172-238",

"http://www.lhmart.com/catalog/s-37-173",
# sports and entertainment
"http://www.lhmart.com/catalog/s-529-530",
"http://www.lhmart.com/catalog/s-529-530-531",

"http://www.lhmart.com/catalog/s-529-535",
"http://www.lhmart.com/catalog/s-529-535-536",
"http://www.lhmart.com/catalog/s-529-535-537",
"http://www.lhmart.com/catalog/s-529-535-538",
"http://www.lhmart.com/catalog/s-529-535-539",
"http://www.lhmart.com/catalog/s-529-535-540",
"http://www.lhmart.com/catalog/s-529-535-541",
"http://www.lhmart.com/catalog/s-529-535-542",

"http://www.lhmart.com/catalog/s-529-543",
"http://www.lhmart.com/catalog/s-529-543-544",
"http://www.lhmart.com/catalog/s-529-543-545",
"http://www.lhmart.com/catalog/s-529-543-546",
"http://www.lhmart.com/catalog/s-529-543-547",
"http://www.lhmart.com/catalog/s-529-543-548",
"http://www.lhmart.com/catalog/s-529-543-549",
"http://www.lhmart.com/catalog/s-529-543-550",
"http://www.lhmart.com/catalog/s-529-543-551",

"http://www.lhmart.com/catalog/s-529-552",
"http://www.lhmart.com/catalog/s-529-552-553",
"http://www.lhmart.com/catalog/s-529-552-554",
"http://www.lhmart.com/catalog/s-529-552-555",
"http://www.lhmart.com/catalog/s-529-552-556",

"http://www.lhmart.com/catalog/s-529-557",
"http://www.lhmart.com/catalog/s-529-557-558",
"http://www.lhmart.com/catalog/s-529-557-559",
"http://www.lhmart.com/catalog/s-529-557-560",
"http://www.lhmart.com/catalog/s-529-557-561",


"http://www.lhmart.com/catalog/s-529-562",
"http://www.lhmart.com/catalog/s-529-562-563",
"http://www.lhmart.com/catalog/s-529-562-564",

"http://www.lhmart.com/catalog/s-529-565",
"http://www.lhmart.com/catalog/s-529-565-566",
"http://www.lhmart.com/catalog/s-529-565-567",
"http://www.lhmart.com/catalog/s-529-565-568",
"http://www.lhmart.com/catalog/s-529-565-569",

"http://www.lhmart.com/catalog/s-529-570",
"http://www.lhmart.com/catalog/s-529-570-571",
"http://www.lhmart.com/catalog/s-529-570-572",
"http://www.lhmart.com/catalog/s-529-570-573",
"http://www.lhmart.com/catalog/s-529-570-574",
"http://www.lhmart.com/catalog/s-529-570-575",
 ]

    def start_requests(self):
        for url in self.start_urls:
            req = urllib2.Request(url)
            print "from start_urls list: "+ url
            result2 = urllib2.urlopen(req, timeout=1000).read()
            soup = BeautifulSoup(result2)
            requirement = re.compile("/product/[0-9]+")
            global aboUrl
            aboUrl = list()
            for add in soup.find_all("a", href=requirement):
                a = add['href']
                b = "http://www.lhmart.com" + a
                if b in aboUrl:
                    print "already exsits"
                else:
                    aboUrl.append(b)
                    print "Crawl successfuly: "+ b
                    yield self.make_requests_from_url(url = b)


    def parse(self, response):
        item = YgItem()
        soup2= BeautifulSoup(response.body)
        item['id'] = soup2.findAll("div", { "class" : "itemcodeprice" })[0].get_text()
        x = soup2.findAll("div", { "class" : "itemproprice" })[0].get_text()
        item['fprice'] = unicodedata.normalize('NFKD', x).encode('ascii','ignore')
        y = soup2.findAll("div", { "class" : "itemmarkprice" })[0].contents[0]
        item['mkprice'] = unicodedata.normalize('NFKD', y).encode('ascii','ignore')
        item['name'] = soup2.findAll("div", { "class" : "itemname" })[0].get_text()
        item['category1'] = soup2.find_all("a", href=re.compile("../catalog/"))[0].contents[0]
        item['category2'] = soup2.find_all("a", href=re.compile("../catalog/"))[1].contents[0]
        item['category3'] = soup2.find_all("a", href=re.compile("../catalog/"))[2].contents[0]
        item['url'] = response._get_url()
        item['date'] = datetime.today().date() + timedelta(days = 1)
       # item['date'] = datetime.today().date() 
        return item

