test = {
  'name': 'list-change',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (list-change 10 '(25 10 5 1))
          ((10) (5 5) (5 1 1 1 1 1) (1 1 1 1 1 1 1 1 1 1))
          scm> (list-change 5 '(4 3 2 1))
          ((4 1) (3 2) (3 1 1) (2 2 1) (2 1 1 1) (1 1 1 1 1))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (list-change 7 '(5 4 3 2 1))
          ((5 2) (5 1 1) (4 3) (4 2 1) (4 1 1 1) (3 3 1) (3 2 2) (3 2 1 1) (3 1 1 1 1) (2 2 2 1) (2 2 1 1 1) (2 1 1 1 1 1) (1 1 1 1 1 1 1))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw06)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
