#ifndef _73229406_c447_43b6_82d6_23bf4b6e594d
#define _73229406_c447_43b6_82d6_23bf4b6e594d

#ifdef _WIN32
#  define EXPORT_DYNAMIC_LIBRARY __declspec(dllexport)
#  define IMPORT_DYNAMIC_LIBRARY __declspec(dllimport)
#else // _WIN32
#  define EXPORT_DYNAMIC_LIBRARY
#  define IMPORT_DYNAMIC_LIBRARY
#endif // _WIN32

#ifdef BUILDING_SYCOMORE
#  define SYCOMORE_API EXPORT_DYNAMIC_LIBRARY
#else // BUILDING_SYCOMORE
#  define SYCOMORE_API IMPORT_DYNAMIC_LIBRARY
#endif // BUILDING_SYCOMORE

#endif // _73229406_c447_43b6_82d6_23bf4b6e594d