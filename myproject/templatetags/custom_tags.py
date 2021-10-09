from django import template


register = template.Library()



# "(bottois\s\w+|hugo\s\w+)/i"
# return f'{self.last_name.capitalize() } {self.first_name.capitalize() }'

#  to optimse
def spotme(authors, me):
  '''
  This function return author string with <span class="me"></span> around me
  me is a name (ex last_name first name)
  authors is a string containing names including me
  '''
  # match regular expression for me and variation
  math = rf"({me.split()[0]}\s\w+|{me.split()[1]}\s\w+)"

  for myname in authors.split(","):
    if re.search(math, myname, re.IGNORECASE):
      authors = authors.replace(myname, f"<span class=\"me\">{myname}</span>")

  return authors


register.filter("spotme",spotme)

import re

def networkIcon(icon_name):
  '''
  return dictionary containing font awesome logo for social network
  '''

  NETWORK_icon = {
    "linkedin":"fab fa-linkedin-square",
    "twitter":"fab fa-twitter-square",
    "github":"fab fa-github-square",
    "medium":"fab fa-medium",
    "website":"fas fa-globe",
    "article":"fas fa-newspaper",
  }

  return NETWORK_icon[icon_name]

register.filter("networkIcon",networkIcon)
