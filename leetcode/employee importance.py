"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import defaultdict

class Solution:
    def getImportance(self, employees: ['Employee'], id: int) -> int:
        employees.sort(key = lambda employee: employee.id)
        
        importance_dict = defaultdict(int)
        subordinates = []
        
        for employee in employees:
            importance_dict[employee.id] = employee.importance
            
            if employee.id == id or employee.id in subordinates:
                subordinates += employee.subordinates
             
        subordinates_importance = 0
        for subordinate in subordinates:
            subordinates_importance += importance_dict[subordinate]
                
        return importance_dict[id] + subordinates_importance
    
        