class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        
        for email in emails:
            local, domain = email.split("@")
            if "+" in local:
                local = local[:local.index("+")]
                        
            local = local.replace(".", "")
            uniqueEmails.add(local + "@" + domain)
            
        return len(uniqueEmails)