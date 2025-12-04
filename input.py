import json
import os


def collect_data():
    person = {
        "name": "age",
        "dob": "religion",
        "address": "country",
        "email": "phone",
    }  # → 必要に応じてデータリストを変更します。

    print("\n===== ENTER DATA =====\n")

    person["name"] = input("[+] Name: ")
    person["age"] = input("[+] Age: ")
    person["dob"] = input("[+] D.O.B: ")
    person["religion"] = input("[+] Religion: ")
    person["address"] = input("[+] Address: ")
    person["country"] = input("[+] Country: ")
    person["email"] = input("[+] Email: ")
    person["phone"] = input("[+] Phone: ")

    return person


def load_existing_data(filename="/result/result.json"):  # → 出力フォルダー
    if os.path.exists(filename):
        with open(filename, "r") as json_file:
            data = json.load(json_file)
            return data
    return []


def save_data_to_json(data, filename="/result/result.json"):  # → 出力フォルダー
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=1)
    print(f"\n→ Folder Location : {filename}\n")


def main():
    existing_data = load_existing_data()
    new_data = collect_data()

    existing_data.append(new_data)

    save_data_to_json(existing_data)


if __name__ == "__main__":
    main()
