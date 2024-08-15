import os
import datetime
import shutil
import mailservice as ms
import validations as v


try:

    # Initializing all the variables 
    today_date = datetime.date.today().strftime("%Y%m%d")
    incoming_files_path = f"../incoming_files/{today_date}"
    email_date = datetime.date.today().strftime("%Y-%m-%d")
    subject = f"Validation email for {email_date}"

    print("print_1:", incoming_files_path)
    # Getting the list of source files from incoming folder for today"s date
    incoming_files = os.listdir(incoming_files_path)
    
    print("print_2:", incoming_files)

    # Directory paths for success and rejected files
    success_files_path = f"../success_files/{today_date}"
    rejected_files_path = f"../rejected_files/{today_date}"

    # Getting the number of files counts
    total_cnt = len(incoming_files)

    # If total_cnt > 0 then start validation else no need to validate files
    if total_cnt > 0:
        print("print_3:", "in total_cnt condition: " + str(total_cnt))
        success_cnt = 0
        rejected_cnt = 0

        # loop through list of files to validate each file 
        for file in incoming_files:
            flag = True  # flag to chec if files validation passed or failed 
            header = False  # flag to check if files has header or not while writing to a error file
            
            # read the master data files and store in product
            products = v.read_master_date()

            with open(f"{incoming_files_path}/{file}") as f:
                orders = f.readlines()[1:] # storing order file data without the header

                # if the file contains any orders then validate each row
                if len(orders) > 0:
                    for order in orders:
                        rejected_reason = ""
                        pid_reject_reason = ""
                        empty_reject_reason = ""
                        date_reject_reason = ""
                        city_reject_reason = ""
                        sales_reject_reason = ""
                        order_dict = {}

                        data_row = order.split(",")
                        order_dict["order_id"] = data_row[0]
                        order_dict["order_date"] = data_row[1]
                        order_dict["product_id"] = data_row[2]
                        order_dict["quantity"] = data_row[3]
                        order_dict["sales"] = data_row[4]
                        order_dict["city"] = data_row[5]

                        val_product_id = v.validate_product_id(order_dict["product_id"], products)
                        val_order_date = v.validate_order_date(order_dict["order_date"])
                        val_city = v.validate_city(order_dict["city"])
                        val_empty = v.validate_emptiness(order_dict)
                        val_sales = v.validate_sales(order_dict)
                        
                        if not val_product_id:
                            pid_reject_reason = f"Invalid product id {order_dict["product_id"]}"
                            rejected_reason = rejected_reason + pid_reject_reason + ";"
                        
                        if len(val_empty) > 0:
                            for col in val_city:
                                empty_reject_reason = empty_reject_reason + col + ";"
                            empty_reject_reason = "Columns " + empty_reject_reason.strip(",") + " are empty."
                            rejected_reason = rejected_reason + empty_reject_reason + ";"
                        
                        if not val_order_date:
                            date_reject_reason = f"Date {order_dict["order_date"]} is a future date."
                            rejected_reason = rejected_reason + date_reject_reason + ";"
                        
                        if not val_city:
                            city_reject_reason = f"Invalid city {order_dict["city"]}."
                            rejected_reason = rejected_reason + city_reject_reason + ";"
                        
                        if not val_sales and val_product_id:
                            sales_reject_reason = f"Invalid Sales Calculation"
                            rejected_reason = rejected_reason + sales_reject_reason
                        
                        if val_product_id and val_order_date and val_city and len(val_empty) ==0 and val_sales:
                            continue
                        else:
                            row_str = ""
                            flag = False
                            if not os.path.exists(f"{rejected_files_path}"):
                                os.mkdirs(f"{rejected_files_path}", exits_ok=True)
                            shutil.copy(f"{incoming_files_path}/{file}", f"{rejected_files_path}/{file}")
                            rejected_cnt += 1
                            with open(f"{rejected_files_path}/error_{file}", "a") as f:
                                for key in order_dict.keys():
                                    row_str = row_str + order_dict["key"] + ","
                                row_str = row_str + rejected_reason
                                row_str = row_str.strip(',')
                                if not header:
                                    f.write('order_id,order_date,product_id,quantity,sales,city,rejected_reason')
                                    f.write('\n')
                                    header = True
                                f.write(row_str)
                                f.write("\n")
                                f.close()
                    else:
                        if flag:
                            print("print_3: in success file write block", )
                            if not os.path.exists(f"{success_files_path}"):
                                os.makedirs(f"{success_files_path}", exist_ok=True)
                            shutil.copy(f"{incoming_files_path}/{file}", f"{success_files_path}/{file}")
                            success_cnt += 1

                else:  # when the file is empty 
                    if not os.path.exists(f'{rejected_files_path}'):
                        os.makedirs(f'{rejected_files_path}', exist_ok=True)
                    shutil.copy(f'{incoming_files_path}/{file}', f'{rejected_files_path}/{file}')       

                    with open(f'{rejected_files_path}/error_{file}', 'a') as f:
                        f.write("Empty file")
                        f.close()
                    rejected_cnt += 1
                    
        else:
            body = f"""
            Total Files: {total_cnt} \n
            Successful Files: {success_cnt} \n
            Rejected Files: {rejected_cnt}
            """
            print(ms.sendmail(subject, body))
            # ms.sendmail(subject, body)
    else:
        print("No file present in source folder.")
        # ms.sendmail(subject, "No file present in source folder.")

except Exception as e:
    print(str(e))

