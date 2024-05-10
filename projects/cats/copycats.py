if typed == source:  # Base cases should go here, you may add more base cases as needed.
      # BEGIN
      return 0
  elif limit <= 0:
      return 1
  elif min(len(typed), len(source)) == 0:
      return max(len(typed), len(source))
      # END
  else:
      if len(typed) < len(source):
          n = len(source) - len(typed)
          if typed + source[:n] == source or source[:n] + typed == source:
              return n
          else:
              if typed[0] == source[0]:
                  return minimum_mewtations(typed[1:], source[1:], limit)
              else:
                  typed = source[0] + typed
                  return 1 + minimum_mewtations(typed[1:], source[1:], limit - 1)
      elif len(typed) > len(source):
          n = len(typed) - len(source)
          if typed[:len(source)] == source or typed[n:] == source:
              return n
          else:
              if typed[0] == source[0]:
                  return minimum_mewtations(typed[1:], source[1:], limit)
              else:
                  typed = typed[1:]
                  return 1 + minimum_mewtations(typed[1:], source[1:], limit - 1)
      elif len(typed) == len(source):
          if len(typed) > 2 and not typed[0] == source[0] and typed[1] == source[1] and typed[2] == source[2]:
              return 1 + minimum_mewtations(typed[1:], source, limit - 1)
          elif typed[0] == source[0]:
              return minimum_mewtations(typed[1:], source[1:], limit)
          else:
              return 1 + minimum_mewtations(typed[1:], source[1:], limit - 1)
