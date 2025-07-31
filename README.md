This script allows you to automatically extract POD (Proof of Delivery) images based on a list of AWB (Air Waybill) numbers stored in an Excel file. It is useful for logistics companies needing to retrieve and send specific delivery proof documents.
🔧 Requirements
Python 3.x
pandas
openpyxl
shutil
os

.
├── images/
│   ├── 123456.jpg
│   ├── 789012.jpg
│   └── ...
├── awb_list.xlsx
└── extract_images.py
