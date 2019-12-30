# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from duckietown_msgs/LEDDetection.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import duckietown_msgs.msg
import genpy

class LEDDetection(genpy.Message):
  _md5sum = "d1ac8691d7a30e838dc372a724aee94b"
  _type = "duckietown_msgs/LEDDetection"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """time timestamp1		# initial timestamp of the camera stream used 
time timestamp2		# final timestamp of the camera stream used 
Vector2D pixels_normalized
float32 frequency 
string color        # will be r, g or b 
float32 confidence  # some value of confidence for the detection (TBD)

# for debug/visualization
float64[] signal_ts
float32[] signal
float32[] fft_fs
float32[] fft

================================================================================
MSG: duckietown_msgs/Vector2D
float32 x
float32 y
"""
  __slots__ = ['timestamp1','timestamp2','pixels_normalized','frequency','color','confidence','signal_ts','signal','fft_fs','fft']
  _slot_types = ['time','time','duckietown_msgs/Vector2D','float32','string','float32','float64[]','float32[]','float32[]','float32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp1,timestamp2,pixels_normalized,frequency,color,confidence,signal_ts,signal,fft_fs,fft

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LEDDetection, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp1 is None:
        self.timestamp1 = genpy.Time()
      if self.timestamp2 is None:
        self.timestamp2 = genpy.Time()
      if self.pixels_normalized is None:
        self.pixels_normalized = duckietown_msgs.msg.Vector2D()
      if self.frequency is None:
        self.frequency = 0.
      if self.color is None:
        self.color = ''
      if self.confidence is None:
        self.confidence = 0.
      if self.signal_ts is None:
        self.signal_ts = []
      if self.signal is None:
        self.signal = []
      if self.fft_fs is None:
        self.fft_fs = []
      if self.fft is None:
        self.fft = []
    else:
      self.timestamp1 = genpy.Time()
      self.timestamp2 = genpy.Time()
      self.pixels_normalized = duckietown_msgs.msg.Vector2D()
      self.frequency = 0.
      self.color = ''
      self.confidence = 0.
      self.signal_ts = []
      self.signal = []
      self.fft_fs = []
      self.fft = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4I3f().pack(_x.timestamp1.secs, _x.timestamp1.nsecs, _x.timestamp2.secs, _x.timestamp2.nsecs, _x.pixels_normalized.x, _x.pixels_normalized.y, _x.frequency))
      _x = self.color
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_f().pack(self.confidence))
      length = len(self.signal_ts)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.signal_ts))
      length = len(self.signal)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.signal))
      length = len(self.fft_fs)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.fft_fs))
      length = len(self.fft)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.fft))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.timestamp1 is None:
        self.timestamp1 = genpy.Time()
      if self.timestamp2 is None:
        self.timestamp2 = genpy.Time()
      if self.pixels_normalized is None:
        self.pixels_normalized = duckietown_msgs.msg.Vector2D()
      end = 0
      _x = self
      start = end
      end += 28
      (_x.timestamp1.secs, _x.timestamp1.nsecs, _x.timestamp2.secs, _x.timestamp2.nsecs, _x.pixels_normalized.x, _x.pixels_normalized.y, _x.frequency,) = _get_struct_4I3f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.color = str[start:end].decode('utf-8')
      else:
        self.color = str[start:end]
      start = end
      end += 4
      (self.confidence,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.signal_ts = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.signal = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.fft_fs = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.fft = struct.unpack(pattern, str[start:end])
      self.timestamp1.canon()
      self.timestamp2.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4I3f().pack(_x.timestamp1.secs, _x.timestamp1.nsecs, _x.timestamp2.secs, _x.timestamp2.nsecs, _x.pixels_normalized.x, _x.pixels_normalized.y, _x.frequency))
      _x = self.color
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_get_struct_f().pack(self.confidence))
      length = len(self.signal_ts)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.signal_ts.tostring())
      length = len(self.signal)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.signal.tostring())
      length = len(self.fft_fs)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.fft_fs.tostring())
      length = len(self.fft)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.fft.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.timestamp1 is None:
        self.timestamp1 = genpy.Time()
      if self.timestamp2 is None:
        self.timestamp2 = genpy.Time()
      if self.pixels_normalized is None:
        self.pixels_normalized = duckietown_msgs.msg.Vector2D()
      end = 0
      _x = self
      start = end
      end += 28
      (_x.timestamp1.secs, _x.timestamp1.nsecs, _x.timestamp2.secs, _x.timestamp2.nsecs, _x.pixels_normalized.x, _x.pixels_normalized.y, _x.frequency,) = _get_struct_4I3f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.color = str[start:end].decode('utf-8')
      else:
        self.color = str[start:end]
      start = end
      end += 4
      (self.confidence,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.signal_ts = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.signal = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.fft_fs = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.fft = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      self.timestamp1.canon()
      self.timestamp2.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4I3f = None
def _get_struct_4I3f():
    global _struct_4I3f
    if _struct_4I3f is None:
        _struct_4I3f = struct.Struct("<4I3f")
    return _struct_4I3f
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
