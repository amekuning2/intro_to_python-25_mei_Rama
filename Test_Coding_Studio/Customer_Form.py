def input_customer(no_batch):
    print("\n=== Customer Form ===")

    id_username = input("ID Username: ")
    name = input("Name: ")
    link = input("Link: ")
    contact = input("Contact: ")

    print("\nPayment Status Options:")
    print("1. Paid")
    print("2. Unpaid")
    print("3. Pending")
    payment_option = input("Choose payment status (1/2/3): ")

    payment_status = {
        "1": "Paid",
        "2": "Unpaid",
        "3": "Pending"
    }.get(payment_option, "Unknown")

    customer_data = {
        "ID Username": id_username,
        "No Batch": no_batch,
        "Name": name,
        "Link": link,
        "Contact": contact,
        "Payment Status": payment_status
    }

    print("\n=== Customer Data Collected ===")
    for key, value in customer_data.items():
        print(f"{key}: {value}")
    
    return customer_data


def main():
    print("=== Start Input Customer Data ===")
    batch_start = 1  # <--- Mulai dari 1
    customers = []

    while True:
        data = input_customer(batch_start)
        customers.append(data)
        batch_start += 1  # Auto-increment batch

        print("\nCustomer added successfully. Waiting for next entry...\n")
        print("-" * 40)


if __name__ == "__main__":
    main()
