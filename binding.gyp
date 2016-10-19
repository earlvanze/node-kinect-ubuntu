{
  'targets': [
    {
      'target_name': 'kinect',
      'sources': [
        'src/kinect.cc',
      ],
      'libraries': [
         'libfreenect.so',
      ],
      'conditions': [
        ['OS=="linux"', {
          'include_dirs': ['/usr/include'],
          'library_dirs': ['/usr/lib'],
        }],
      ]
    }
  ]
}
