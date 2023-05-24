import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox


# Define a function to open the login window
def open_login_window():
    # Create a new tkinter window
    login_window = tk.Tk()
    login_window.title("Login Window")
    login_window.geometry("300x200")

    # Define a function to check the credentials
    def check_credentials():
        username = username_entry.get()
        password = password_entry.get()

        # TODO: Check the credentials against the database
        # For this example, the hardcoded username/password is "admin"
        # if username == "" and password == "":
        if username == "admin" and password == "password":
            login_window.destroy()
            open_main_window()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    # Add a label to the login window
    label = tk.Label(login_window, text="Enter your credentials")
    label.pack(pady=10)

    # Add a username entry to the login window
    username_label = tk.Label(login_window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    # Add a password entry to the login window
    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    # Add a login button to the login window
    login_button = tk.Button(login_window, text="Login", command=check_credentials)
    login_button.pack(pady=10)

    login_window.mainloop()


# Define a function to open the main window
def open_main_window():
    # Create a new tkinter window
    main_window = tk.Tk()
    main_window.title("Main Window")
    main_window.geometry("800x500")

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="dbms_project"
    )
    # Add a label to the main window
    # label = tk.Label(main_window, text="Welcome to the Database!", font=("Arial", 20))
    label = tk.Label(main_window, text="Database", font=("Arial", 20))
    label.pack()
    mycursor = mydb.cursor()

    # Define a function to create a new tab
    # Define a function to create a new tab
    def create_tab(tab_name):
        # Create a new tab
        tab = ttk.Frame(notebook)
        notebook.add(tab, text=tab_name)

        if tab_name == "welcome tab":
            table_label1 = tk.Label(tab, text="WELCOME TO THE DATABASE", font=("Arial", 20))
            table_label2 = tk.Label(tab, text="select from above tabs to see all tables of database",
                                    font=("Arial", 20))
            table_label1.pack()
            table_label2.pack()

        elif tab_name == "joined table":
            label = tk.Label(tab, text=f"{tab_name} table: ", font=("Arial", 20))
            label.pack(pady=10)

            mycursor.execute(
                f"SELECT si.name, si.roll, si.email, si.contact, si.address, si.birthdate, si.gender, c.course, c.stream, sc.semester, sc.cgpa, sh.roll, sh.hobby, sh.about FROM student_info si JOIN student_course sc ON si.roll = sc.roll JOIN course c ON sc.courseid = c.courseid LEFT JOIN student_hobbies_about sh ON si.roll = sh.roll;")

            rows = mycursor.fetchall()

            columns = [desc[0] for desc in mycursor.description]

            # Create a Treeview widget to display the data
            treeview = ttk.Treeview(tab, show="headings", columns=columns)
            # # treeview.pack(side="left", fill="both", expand=True)
            treeview.pack(side='top', fill="x")

            # Add the columns to the Treeview widget
            for col in columns:
                treeview.heading(col, text=col.title(), anchor='nw')
                treeview.column(col, anchor='nw', stretch=True)

            # Add the rows to the Treeview widget
            for row in rows:
                treeview.insert("", "end", values=row)

            label1 = tk.Label(tab,
                              text=f"The values in this(joined) table is same as original table(form data table) hence it is lossless decomposition",
                              font=("Arial", 15))
            label1.pack(pady=10)



        elif tab_name == "Student Info" or tab_name == "form data":
            # Add a label to the tab
            label = tk.Label(tab, text=f"{tab_name} table: ", font=("Arial", 20))
            label.pack(pady=10)

            mycursor.execute(f"SELECT * FROM {tab_name.replace(' ', '_')}")

            rows = mycursor.fetchall()

            columns = [desc[0] for desc in mycursor.description]

            # Create a Treeview widget to display the data
            treeview = ttk.Treeview(tab, show="headings", columns=columns)
            # # treeview.pack(side="left", fill="both", expand=True)
            treeview.pack(side='top', fill="x")

            # Add the columns to the Treeview widget
            for col in columns:
                treeview.heading(col, text=col.title(), anchor='nw')
                treeview.column(col, anchor='nw', stretch=True)

            # Add the rows to the Treeview widget
            for row in rows:
                treeview.insert("", "end", values=row)

            button_frame = tk.Frame(tab)
            button_frame.pack(side="top", pady=10)

            table_label5 = tk.Label(
                tab, text="select the row to be deleted from above table and press the corresponding buttons below:",
                font=("Arial", 15))
            table_label5.pack()

            button_frame = tk.Frame(tab)
            button_frame.pack(side="top", pady=10)

            # update_button = tk.Button(button_frame, text="Update Query",
            #                           command=lambda: update_query(tab_name.replace(' ', '_'), treeview))
            # update_button.pack(side="left", padx=5)

            delete_button = tk.Button(button_frame, text="Delete Query",
                                      command=lambda: delete_query(tab_name.replace(' ', '_'), treeview))
            delete_button.pack(side="left", padx=5)

            table_label6 = tk.Label(tab, text="", font=("Arial", 14))
            table_label6.pack()
            table_label6 = tk.Label(tab, text="", font=("Arial", 14))
            table_label6.pack()
            table_label6 = tk.Label(tab, text="", font=("Arial", 14))
            table_label6.pack()

            table_label4 = tk.Label(
                tab, text="enter the id(roll number of student) to search from above table table:", font=("Arial", 15))
            table_label4.pack()

            search_frame = tk.Frame(tab)
            search_frame.pack(side="top", pady=10)

            search_textfield = tk.Entry(search_frame)
            search_textfield.pack(side="left", padx=5)

            search_button = tk.Button(search_frame, text="Search Query",
                                      command=lambda: search_query(tab_name.replace(' ', '_'), treeview,
                                                                   search_textfield))
            search_button.pack(side="left", padx=5)

        else:
            # Add a label to the tab
            label = tk.Label(tab, text=f"{tab_name} table: ", font=("Arial", 20))
            label.pack(pady=10)

            mycursor.execute(f"SELECT * FROM {tab_name.replace(' ', '_')}")

            rows = mycursor.fetchall()

            columns = [desc[0] for desc in mycursor.description]

            # Create a Treeview widget to display the data
            treeview = ttk.Treeview(tab, show="headings", columns=columns)
            # # treeview.pack(side="left", fill="both", expand=True)
            treeview.pack(side='top', fill="x")

            # Add the columns to the Treeview widget
            for col in columns:
                treeview.heading(col, text=col.title(), anchor='nw')
                treeview.column(col, anchor='nw', stretch=True)

            # Add the rows to the Treeview widget
            for row in rows:
                treeview.insert("", "end", values=row)


            if tab_name != "Course":
                button_frame = tk.Frame(tab)
                button_frame.pack(side="top", pady=10)

                table_label5 = tk.Label(
                    tab,
                    text="select the row to be updated/deleted from above table and press the corresponding buttons below:",
                    font=("Arial", 15))
                table_label5.pack()

                button_frame = tk.Frame(tab)
                button_frame.pack(side="top", pady=10)

                update_button = tk.Button(button_frame, text="Update Query",
                                          command=lambda: update_query(tab_name.replace(' ', '_'), treeview))
                update_button.pack(side="left", padx=5)

                delete_button = tk.Button(button_frame, text="Delete Query",
                                          command=lambda: delete_query(tab_name.replace(' ', '_'), treeview))
                delete_button.pack(side="left", padx=5)

                table_label6 = tk.Label(tab, text="", font=("Arial", 14))
                table_label6.pack()
                table_label6 = tk.Label(tab, text="", font=("Arial", 14))
                table_label6.pack()
                table_label6 = tk.Label(tab, text="", font=("Arial", 14))
                table_label6.pack()

                table_label4 = tk.Label(
                    tab, text="enter the id(roll number of student) to search from above table table:",
                    font=("Arial", 15))
                table_label4.pack()

                search_frame = tk.Frame(tab)
                search_frame.pack(side="top", pady=10)

                search_textfield = tk.Entry(search_frame)
                search_textfield.pack(side="left", padx=5)

                search_button = tk.Button(search_frame, text="Search Query",
                                          command=lambda: search_query(tab_name.replace(' ', '_'), treeview,
                                                                       search_textfield))
                search_button.pack(side="left", padx=5)

                return tab

    def search_query(tab_name, treeview, search_textfield):
        # Get the text from the search Text widget
        # search_text = search_textfield.get("1.0", tk.END).strip()
        search_text = search_textfield.get().strip()
        print(search_text)

        # Return if search text is empty
        if not search_text:
            return

        # Remove all previous search results from the treeview
        treeview.delete(*treeview.get_children())

        # Execute the search query
        mycursor.execute(f"SELECT * FROM {tab_name} WHERE roll = '{search_text}'")
        rows = mycursor.fetchall()

        # Add the search results to the Treeview widget
        for row in rows:
            treeview.insert("", "end", values=row)

    def update_query(tab_name, treeview):
        # Get the selected row
        selected_item = treeview.focus()
        if not selected_item:
            messagebox.showerror("Error", "Please select a row to update.")
            return

        # Get the values of the selected row
        # values = treeview.item(selected_item, "values")

        # Get the primary key of the selected row
        # primary_key = values[0]
        values = treeview.item(selected_item, 'values')
        # print(enumerate(treeview["columns"]))
        roll_value_update = None
        for i, col in enumerate(treeview["columns"]):
            if col == "roll":
                roll_value_update = values[i]
                break
            elif col == "Roll":
                roll_value_update = values[i]
                break
            if roll_value_update is None:
                messagebox.showerror("Error", "Roll number column not found1.")
                return

        primary_key = roll_value_update
        print(primary_key)

        # Open a new window for the user to input the updated values
        update_window = tk.Toplevel(main_window)
        update_window.title(f"Update {tab_name} Row")

        # Create a form for the user to input the updated values
        update_form = tk.Frame(update_window)

        # Execute the SELECT query and consume the result
        mycursor.execute(f"SELECT * FROM {tab_name.replace(' ', '_')} WHERE roll=%s", (primary_key,))
        row = mycursor.fetchone()
        if not row:
            messagebox.showerror("Error", "Row not found.")
            print(f"No row found for primary key {primary_key} in table {tab_name}.")
            print(f"with parameter {primary_key}.")
            return

        # Get the column names
        columns = [desc[0] for desc in mycursor.description]

        entry_list = []

        for i, col in enumerate(columns):
            label = tk.Label(update_form, text=col.title())
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            entry = tk.Entry(update_form, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entry.insert(0, row[i])

            entry_list.append(entry)

        update_form.pack()

        def submit_update():
            values = treeview.item(selected_item, 'values')
            roll_value_update = None
            for i, col in enumerate(treeview["columns"]):
                if col == "roll":
                    roll_value_update = values[i]
                    break
            if roll_value_update is None:
                messagebox.showerror("Error", "Roll number column not found2.")
                return

            # Get the new values from the form
            new_values = [entry.get() for entry in entry_list]

            # Construct the update query
            update_query = f"UPDATE {tab_name.replace(' ', '_')} SET "

            for i, col in enumerate(columns):
                update_query += f"{col}='{new_values[i]}'"
                if i != len(columns) - 1:
                    update_query += ", "

            update_query += f" WHERE roll='{roll_value_update}'"

            # Execute the UPDATE query and consume the result
            mycursor.execute(update_query)
            mycursor.fetchall()
            mydb.commit()

            # Update the Treeview widget with the new values
            for i, value in enumerate(new_values):
                treeview.set(selected_item, columns[i], value)

            messagebox.showinfo(
                "Success", f"{tab_name.title()} row updated successfully.")
            update_window.destroy()

        # Add a button to submit the update
        submit_button = tk.Button(
            update_form, text="Update", command=submit_update)
        submit_button.grid(row=len(columns), column=0, columnspan=2, padx=10, pady=10)
        print("Created update form")
        update_form.pack()
        print("Packed update form")

    def delete_query(tab_name, treeview):
        # Get the selected row(s) from the Treeview widget
        selected = treeview.selection()
        if not selected:
            messagebox.showerror("Error", "Please select a row to delete.")
            return

        # Get the primary key column name of the table
        mycursor.execute(f"SHOW KEYS FROM {tab_name.replace(' ', '_')} WHERE Key_name = 'PRIMARY'")
        primary_key = mycursor.fetchone()[4]
        mycursor.fetchall()

        # Delete the selected row(s) from the database
        for item in selected:
            values = treeview.item(item, 'values')
            roll_value = None
            for i, col in enumerate(treeview["columns"]):
                if col == "roll":
                    roll_value = values[i]
                    break
            if roll_value is None:
                messagebox.showerror("Error", "Roll number column not found3.")
                return
            mycursor.execute(f"DELETE FROM {tab_name.replace(' ', '_')} WHERE {primary_key} = '{roll_value}'")
            mydb.commit()

            # Delete the selected row(s) from the Treeview widget
            treeview.delete(item)

    # Create a notebook to hold the tabs
    notebook = ttk.Notebook(main_window)
    notebook.pack(fill='both', expand=True)

    # Create the tabs
    create_tab("welcome tab")
    create_tab("Student Info")
    create_tab("Course")
    create_tab("Student Course")
    create_tab("Student Hobbies about")
    create_tab("form data")
    create_tab("joined table")

    main_window.mainloop()


open_login_window()