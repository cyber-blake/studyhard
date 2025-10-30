from tasks import *
import pytest
import datetime


# * Задача 1
# * 1.1
@pytest.fixture
def sample_task():
    sample_task = Task("test task")
    return sample_task


def test_task_initialization(sample_task):
    print(sample_task)
    assert sample_task.priority == 1


def test_task_completed(sample_task):
    assert sample_task.is_completed == False


def test_task_deadline(sample_task):
    assert sample_task.deadline == None


# * 1.2
def test_task_completed2(sample_task):
    sample_task.mark_completed()
    result = str(sample_task)
    assert "Completed" in result


# * 1.3
@pytest.fixture
def get_date():
    return datetime.date(2012, 12, 30)


def test_task_deadline_2(sample_task, get_date):
    sample_task.deadline = datetime.datetime(1999, 12, 31)
    sample_task.set_deadline(get_date)
    assert sample_task.deadline == get_date


# * 1.4
def test_task_string_repr(sample_task):
    result = sample_task.__str__()
    assert "Description:" in result
    assert "Priority: 1" in result
    assert "Status: Not Completed" in result
    assert "No Deadline" in result


# * 1.5
@pytest.fixture
def task_list():
    new_list = TaskList()
    return new_list


def test_tasklist_init(task_list):
    assert len(task_list.tasks) == 0


# * 1.6
def test_add_task(task_list, sample_task):
    task_list.add_task(sample_task)
    assert len(task_list.tasks) == 1
    assert sample_task in task_list.tasks


# * 1.7
def test_remove_task(sample_task, task_list):
    task_list.add_task(sample_task)
    init_len = len(task_list.tasks)
    task_list.remove_task(sample_task)
    final_len = len(task_list.tasks)
    assert final_len == init_len - 1
    assert sample_task not in task_list.tasks


# * 1.8
@pytest.fixture
def task1():
    task1 = Task("Lorem ipsum", 3)
    return task1


@pytest.fixture
def task2():
    task2 = Task("dolores prodet", 2)
    return task2


def test_sort_by_priority(task_list, task1, task2):
    task_list.add_task(task1)
    task_list.add_task(task2)
    task_list.sort_by_priority()
    task1 = task_list.tasks[0]
    task2 = task_list.tasks[1]
    assert task1.priority < task2.priority


# * 1.9
def test_filter_by_status(task_list, task1, task2):
    task_list.add_task(task1)
    task1.mark_completed()
    task_list.add_task(task2)
    completed = task_list.filter_by_status(completed=True)
    assert task1 in task_list.tasks and len(completed) == 1
