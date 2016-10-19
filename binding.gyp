{
  'targets': [
    {
      'target_name': 'kinect',
      'sources': [
        'src/kinect.cc',
      ],
      'libraries': [
         '/usr/lib/libfreenect.so',
      ],
       'include_dirs': [
         '/usr/include'
      ],
       'library_dirs': [
         '/usr/lib'
      ],
    }
  ]
}
