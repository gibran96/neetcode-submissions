import re
class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        cache = {}
        visit = set()
        mapping = {k: v for k,v in replacements}
        
        def resolve(key):
            if key in cache:
                return cache[key]
            
            if key in visit:
                raise ValueError(f"cycle detected at {key}")
            
            if key not in mapping:
                raise ValueError(f"unknown key found {key}")

            visit.add(key)

            value = re.sub(
                r"%(\w+)%",
                lambda match: resolve(match.group(1)),
                mapping[key]
            )

            visit.remove(key)
            cache[key] = value

            return value
        
        return re.sub(
            r"%(\w+)%",
            lambda match: resolve(match.group(1)),
            text
        )


            
