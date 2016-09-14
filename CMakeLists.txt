
cmake_minimum_required(VERSION 3.5.0)
project(cmaketest)

find_package(Qt5Core REQUIRED)

execute_process(
  COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/generator.py --list
    ${CMAKE_CURRENT_BINARY_DIR}/genoutput
    ${CMAKE_CURRENT_SOURCE_DIR}/fileWithNumber
  OUTPUT_VARIABLE fileList
)

set_property(DIRECTORY PROPERTY CMAKE_CONFIGURE_DEPENDS
    ${CMAKE_CURRENT_SOURCE_DIR}/generator.py
    ${CMAKE_CURRENT_SOURCE_DIR}/fileWithNumber
)

string(REPLACE "\n" ";" fileList ${fileList})

add_custom_command(OUTPUT ${fileList}
  COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/generator.py
    ${CMAKE_CURRENT_BINARY_DIR}/genoutput
    ${CMAKE_CURRENT_SOURCE_DIR}/fileWithNumber
  DEPENDS
    ${CMAKE_CURRENT_SOURCE_DIR}/generator.py
    ${CMAKE_CURRENT_SOURCE_DIR}/fileWithNumber
)

qt5_wrap_cpp(moc_files ${fileList})

add_executable(servertest servertest.cpp ${fileList} ${moc_files})
target_link_libraries(servertest Qt5::Core)
target_include_directories(servertest PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/genoutput)
