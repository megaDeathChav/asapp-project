'''
This program creates a JSON file with the 'true' values of customer data (name, phone, email).
If the attribute is not present in the text, it will set the value to "NOT_PRESENT"
Change the file name to the desired dataset (filepath may be different on other machines).

Output: predicted_ans.json
'''

import json

main_filename = './smaller_datasets/80_10_10.json'

def process_null(file):
    with open(file, 'r') as file:
        data = json.load(file)

    # Collecting details in a dictionary format
    output_data = {"train": []}

    for convo in data["train"]:
        curr_details = {}
        
        full_conversation = ''
        for excerpt in convo["original"]:
            full_conversation += ("".join(excerpt) + " ")

        full_conversation = full_conversation.lower()

        # Check for customer_name
        if "customer_name" in convo["scenario"]["personal"] and convo["scenario"]["personal"]["customer_name"].lower() in full_conversation:
            curr_details["customer_name"] = convo["scenario"]["personal"]["customer_name"]
        else:
            curr_details["customer_name"] = 'NOT_PRESENT'

        # Check for phone
        if "phone" in convo["scenario"]["personal"] and convo["scenario"]["personal"]["phone"] in full_conversation:
            curr_details["phone"] = convo["scenario"]["personal"]["phone"]
        else:
            curr_details["phone"] = 'NOT_PRESENT'

        # Check for email
        if "email" in convo["scenario"]["personal"] and convo["scenario"]["personal"]["email"].lower() in full_conversation:
            curr_details["email"] = convo["scenario"]["personal"]["email"]
        else:
            curr_details["email"] = 'NOT_PRESENT'
        
        # Append each detail dictionary to output_data
        output_data["train"].append(curr_details)

    # Write the entire output_data dictionary as JSON
    with open('predicted_ans.json', 'w') as f:
        json.dump(output_data, f, indent=4)

process_null(main_filename)
