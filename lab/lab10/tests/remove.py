test = {
  'name': 'remove',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (remove 3 nil)
          ()
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (remove 2 '(1 3 2))
          (1 3)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (remove 1 '(1 3 2))
          (3 2)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (remove 42 '(1 3 2))
          (1 3 2)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (remove 3 '(1 3 3 7))
          (1 7)
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
