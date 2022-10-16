from datetime import datetime
from main import main


def test__time():
    time_start = datetime.now()
    main()
    time_end = datetime.now()
    print(f"Время выполнения равняется {(time_end - time_start)}")


if __name__ == '__main__':
    test__time()
