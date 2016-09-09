
cmake_minimum_required(VERSION 3.5.0)
project(cmaketest)

find_package(Qt5Core REQUIRED)

execute_process(
  COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/generator.py --list ${CMAKE_CURRENT_BINARY_DIR}/genoutput 5
  OUTPUT_VARIABLE fileList
)

string(REPLACE "\n" ";" fileList ${fileList})

add_custom_command(OUTPUT ${fileList}
  COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/generator.py ${CMAKE_CURRENT_BINARY_DIR}/genoutput 5
)

qt5_wrap_cpp(moc_files ${fileList})

add_executable(servertest servertest.cpp ${fileList} ${moc_files})
target_link_libraries(servertest Qt5::Core)
target_include_directories(servertest PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/genoutput)
