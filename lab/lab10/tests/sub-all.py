test = {
  'name': 'sub-all',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (sub-all '(go ((bears))) '(go bears) '(big game))
          (big ((game)))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (sub-all '((4 calling birds) (3 french hens) (2 turtle doves))
          ....     '(1 2 3 4)
          ....     '(one two three four))
          ((four calling birds) (three french hens) (two turtle doves))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab10)
      scm> (load 'lab10_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
