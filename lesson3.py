class Developer:
    def __init__(self, solary, position, hours_per_day):
        self.solary = solary
        self.position = position
        self.hours_per_day = hours_per_day

    def return_information(self):
        return f"Solary: {self.solary}, Position: {self.position}, Hours per Day: {self.hours_per_day}"


class FrontendDeveloper(Developer):
    def __init__(self, solary, hours_per_day):
        super().__init__(solary, "Frontend Developer", hours_per_day)

    def return_information(self):
        return super().return_information()


class BackendDeveloper(Developer):
    def __init__(self, solary, hours_per_day):
        super().__init__(solary, "Backend Developer", hours_per_day)

    def return_information(self):
        return super().return_information()


backend_developer = BackendDeveloper(solary=50000, hours_per_day=10)
frontend_developer = FrontendDeveloper(solary=40000, hours_per_day=11)

print(backend_developer.return_information())
print(frontend_developer.return_information())
