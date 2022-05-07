# Task 3: Boarding Factory

In the file [`src/task_3_boarder_factory`](src/task_3_boarder_factory.py), create a factory class `BoarderFactory`:
- [ ] The factory class has one static method `create_object(boarder_type, *args, **kwargs)`.
- [ ] If `boarder_type` is not equal to `"Pilot"` or `"Crew"` or `"Passenger"` then `create_object(...)` shows an error message.
- [ ] with if statements and depending on the type of `boarder_type`, the method `create_object(...)` returns an object of the class `Pilot` or `Crew` or `Passenger`. 
