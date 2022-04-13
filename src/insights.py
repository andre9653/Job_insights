from src.jobs import read


def get_unique_job_types(path):
    csv_read = read(path)
    unique_jobs = []
    for job in csv_read:
        if job['job_type'] not in unique_jobs:
            unique_jobs.append(job['job_type'])
    return unique_jobs


def filter_by_job_type(jobs, job_type):
    type_jobs = []
    for job in jobs:
        if job_type == job['job_type']:
            type_jobs.append(job)
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return type_jobs


def get_unique_industries(path):
    csv_read = read(path)
    unique_industry = set()
    for job in csv_read:
        if job['industry'] and job['industry'] not in unique_industry:
            unique_industry.add(job['industry'])
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    return unique_industry


def filter_by_industry(jobs, industry):
    all_industry = []
    for job in jobs:
        if industry == job['industry']:
            all_industry.append(job)
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return all_industry


def get_max_salary(path):
    csv_read = read(path)
    all_salary = []
    for job in csv_read:
        if any(chr.isdigit() for chr in job['max_salary']):
            all_salary.append(int(job['max_salary']))
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    return max(all_salary)


def get_min_salary(path):
    csv_read = read(path)
    all_salary = []
    for job in csv_read:
        if any(chr.isdigit() for chr in job['min_salary']):
            all_salary.append(int(job['min_salary']))
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    return min(all_salary)


def matches_salary_range(job, salary):
    if 'min_salary' not in job or 'max_salary'not in job:
        raise ValueError("err")
    elif type(job['min_salary']) != int or type(job['max_salary']) != int:
        raise ValueError("err")
    elif job['min_salary'] > job['max_salary']:
        raise ValueError("err")
    elif type(salary) != int:
        raise ValueError("err")
    return job['min_salary'] <= salary <= job['max_salary']

    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """


def filter_by_salary_range(jobs, salary):
    all_jobs = []

    for job in jobs:
        if type(salary) == int:
            if job["min_salary"] <= salary <= job["max_salary"]:
                all_jobs.append(job)

    return all_jobs
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
