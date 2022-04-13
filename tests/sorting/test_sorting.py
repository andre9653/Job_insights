from src.sorting import sort_by


jobs = [
    {
        "min_salary": 1000,
        "max_salary": 1500,
        "date_posted": "2022-01-20",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == 1000

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 15000

    sort_by(jobs, "min_salary")
    assert jobs[0]["date_posted"] == "2022-01-20"
