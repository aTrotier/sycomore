set BUILD_DIR=%WORKSPACE%\build
set INSTALL_DIR=%WORKSPACE%\install

for /f "tokens=*" %%a in ( '%PYTHON% -c "from distutils.sysconfig import *; print(get_python_lib(True, prefix=\"\"))"' ) do set PYTHONPATH=%INSTALL_DIR%\%%a
echo %PYTHONPATH%

set PATH=%PATH%;C:\Libraries\boost_1_67_0\lib32-msvc-14.1;%INSTALL_DIR%\bin

set SYCOMORE_TEST_DATA=%WORKSPACE%\tests\data

cd %BUILD_DIR%
ctest -T Test
%PYTHON% -m unittest discover -s %WORKSPACE%/tests/python/

cd %WORKSPACE%
