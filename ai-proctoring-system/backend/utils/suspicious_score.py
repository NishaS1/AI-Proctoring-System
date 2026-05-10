class SuspiciousScore:
    def __init__(self):
        self.score = 0
        self.events = []

    def add_event(self, event):
        weights = {
            'looking_away': 2,
            'multiple_faces': 5,
            'object_detected': 10,
            'talking': 3
        }
        self.score += weights.get(event, 0)
        self.events.append(event)

    def get_score(self):
        return self.score

    def get_report(self):
        return {
            'score': self.score,
            'events': self.events,
            'flagged': self.score > 15
        }