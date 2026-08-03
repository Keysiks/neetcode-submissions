class TimeMap:

    def __init__(self):
        self._store: dict[str, tuple[list]] = {} # ([value], [timestamp])

    def set(self, key: str, value: str, timestamp: int) -> None:
        values, times = self._store.setdefault(key, ([], []))
        values.append(value)
        times.append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._store:
            return ""
        values, times = self._store[key]
        l, r = 0, len(times)
        while l + 1 < r:
            mid = (l + r) // 2
            if times[mid] > timestamp:
                r = mid
            else:
                l = mid
        return values[l] if times[l] <= timestamp else ""


        
