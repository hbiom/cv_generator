from django import template


register = template.Library()


#  to optimse
def spotme(author, me):
  '''
  me is a single name
  author is a string containing names including me
  This function return author string with <span></span> around me
  '''
  return author.replace(me, f"<span class=\"me\">{me}</span>")


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
  }

  return NETWORK_icon[icon_name]

register.filter("networkIcon",networkIcon)


