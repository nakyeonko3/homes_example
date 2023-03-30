import pandas as pd

# import csv
import csv


def create_txt_to_csv():
    filename = "household_power_consumption2.csv"
    new_filename = "household_power_consumption3.csv"
    read_file = pd.read_csv(filename)
    read_file.to_csv(new_filename, index=None)


def drop_colum():
    # 파일 경로 지정
    filename = "household_power_consumption2.csv"
    new_filename = "household_power_consumption3.csv"

    # 삭제할 열의 인덱스 리스트
    # 예를 들어, 1번과 3번 열을 삭제하려면 [1, 3]으로 설정합니다.
    columns_to_remove = [4, 5, 6, 7, 8, 9]

    # 새로운 데이터를 저장할 리스트
    new_data = []

    # CSV 파일 열기
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)

        # CSV 파일의 각 행에 대해 반복
        for row in csvreader:
            # 삭제할 열의 인덱스를 제외한 데이터만 새로운 리스트에 추가
            new_row = [row[i] for i in range(len(row)) if i not in columns_to_remove]
            new_data.append(new_row)

    # 새로운 데이터를 CSV 파일에 쓰기
    with open(new_filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(new_data)


def merge_column():
    # CSV 파일 읽기
    filename = "household_power_consumption3.csv"
    new_filename = "household_power_consumption4.csv"
    df = pd.read_csv(filename)

    # 두 열 병합하여 새로운 열 생성
    df["timestamp"] = df["Date"] + " " + df["Time"]

    # 새로운 CSV 파일 저장
    df.to_csv(new_filename, index=False)


def reorder_columns():
    filename = "household_power_consumption4.csv"
    new_filename = "household_power_consumption5_reorder.csv"
    df = pd.read_csv(filename)
    df = df.reindex(columns=["timestamp", "Global_reactive_power"])
    df.to_csv(new_filename, index=False)


def limit_rows():
    filename = "household_power_consumption5_reorder.csv"
    new_filename = "household_power_consumption7_limited.csv"
    df = pd.read_csv(filename)
    df = df.drop(df.index[10000:])
    df.to_csv(new_filename, index=False)


if __name__ == "__main__":
    # merge_column()
    # reorder_columns()
    limit_rows()
