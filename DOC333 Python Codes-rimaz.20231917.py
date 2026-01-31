# XYZ Company
ongoing_projects = []
completed_projects = []
available_workers = []

no_of_workers = int(input("No of Workers: "))  # Enter number of workers

while True:
    print("XYZ Company".center(50))
    print("Main Menu".center(50))
    print("1. Add a new project to existing projects.")
    print("2. Remove a completed project from existing projects.")
    print("3. Add new workers to available workers group.")
    print("4. Update details on ongoing projects.")
    print("5. Project Statistics")
    print("6. Exit")

    choice = int(input("Your Choice: "))

    if choice == 1:
        print("XYZ Company".center(50))
        print("Add a new project".center(50))
        project_code = input("Project Code (Enter '0' to exit): ")
        if project_code != '0':
            clients_name = input("Clients Name: ")
            start_date = input("Start date(DD-MM-YY): ")
            expected_end_date = input("Expected end date(DD-MM-YY): ")
            number_of_workers = int(input("Number of workers: "))

            # Check workers availability
            if number_of_workers >= no_of_workers:
                projected_status = input("Project status(ongoing, on hold or completed): ")
                project = {
                    "project_code": project_code,
                    "clients_name": clients_name,
                    "start_date": start_date,
                    "expected_end_date": expected_end_date,
                    "number_of_workers": number_of_workers,
                    "projected_status": projected_status,
                }
                ongoing_projects.append(project)

                # Update available workers
                no_of_workers -= number_of_workers

                save_project = input("Do you want to save the project (Yes/No)? ").lower()
                if save_project == 'no':
                    ongoing_projects.remove(project)
                    no_of_workers += number_of_workers
                    print("Project not saved successfully.")
                else:
                    print("Project saved successfully.")
            else:
                print("Insufficient workers to start the project. Project not started.")
        else:
            print("Project not started.")
                
    elif choice == 2:
        print("XYZ Company".center(50))
        print("Remove Completed Project".center(50))
        project_code = input("Project Code: ")
        remove = input("Do you want to remove the project (Yes/No)? ").lower()
        if remove == "yes":
            for project in ongoing_projects:
                if project["project_code"] == project_code:
                    ongoing_projects.remove(project)
                    completed_projects.append(project)
                    # Release the workers 
                    available_workers.extend([None] * project["number_of_workers"])
                    print("Project removed successfully")
                    break
            else:
                print("Project not found in ongoing projects.")
        else:
            print("Project not removed successfully")

    elif choice == 3:
        print("XYZ Company".center(50))
        print("Add new workers".center(50))
        workers_to_add = int(input("Number of workers to add: "))

        if workers_to_add > 0:
            want_to_add = input("Do you want to add (Yes/No)? ").lower()
            if want_to_add == "yes":
                available_workers += ["Worker" + str(i) for i in range(1, workers_to_add + 1)]
                print("Workers added successfully")
            else:
                    print("Workers not added")
        else:
            print("Invalid number of workers.")

    elif choice == 4:
        print("XYZ Company".center(50))
        print("Update Project Details".center(50))
        project_code = input("Project Code (Enter '0' to exit): ")
        if project_code != '0':
            for project in ongoing_projects:
                if project["project_code"] == project_code:
                    clients_name = input("Clients Name: ")
                    start_date = input("Start date(DD-MM-YY): ")
                    expected_end_date = input("Expected end date(DD-MM-YY): ")
                    number_of_workers = int(input("Number of workers: "))
                    projected_status = input("Project status(ongoing, on hold or completed): ")
                    update = input("Do you want to update the project details (Yes/No)? ").lower()
                    if update == "yes":
                        # Release the current workers 
                        available_workers.extend([None] * project["number_of_workers"])
                        project.update({
                            "clients_name": clients_name,
                            "start_date": start_date,
                            "expected_end_date": expected_end_date,
                            "number_of_workers": number_of_workers,
                            "projected_status": projected_status,
                        })
                        # Update the available workers
                        available_workers = available_workers[:len(available_workers) - number_of_workers]
                        print("Project details updated successfully")
                    else:
                        print("Project details not updated successfully")
                    break
            else:
                print("Project not found in ongoing projects.")

    elif choice == 5:
        print("XYZ Company".center(50))
        print("Project Statistics".center(50))
        ongoing_projects_count = len(ongoing_projects)
        completed_projects_count = len(completed_projects)
        available_workers_count = len(available_workers)
        print(f"Number of ongoing projects: {ongoing_projects_count}")
        print(f"Number of completed projects: {completed_projects_count}")
        print(f"Number of available workers to assign: {available_workers_count}")
        
        add_project = input("Do you want to add the project (Yes/No)? ").lower()
        if add_project == "yes":
            print("Project added successfully.")
        else:
            print("Project not added successfully.")

    elif choice == 6:
        print("Exiting Code")
        break

