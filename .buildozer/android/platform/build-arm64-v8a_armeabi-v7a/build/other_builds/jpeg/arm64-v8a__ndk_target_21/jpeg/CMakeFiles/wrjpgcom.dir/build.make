# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg

# Include any dependencies generated for this target.
include CMakeFiles/wrjpgcom.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/wrjpgcom.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/wrjpgcom.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/wrjpgcom.dir/flags.make

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o: CMakeFiles/wrjpgcom.dir/flags.make
CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o: wrjpgcom.c
CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o: CMakeFiles/wrjpgcom.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o"
	/home/anarchking/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang --target=aarch64-none-linux-android21 --sysroot=/home/anarchking/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/sysroot $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o -MF CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o.d -o CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o -c /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg/wrjpgcom.c

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/wrjpgcom.dir/wrjpgcom.c.i"
	/home/anarchking/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang --target=aarch64-none-linux-android21 --sysroot=/home/anarchking/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/sysroot $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg/wrjpgcom.c > CMakeFiles/wrjpgcom.dir/wrjpgcom.c.i

CMakeFiles/wrjpgcom.dir/wrjpgcom.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/wrjpgcom.dir/wrjpgcom.c.s"
	/home/anarchking/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang --target=aarch64-none-linux-android21 --sysroot=/home/anarchking/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/sysroot $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg/wrjpgcom.c -o CMakeFiles/wrjpgcom.dir/wrjpgcom.c.s

# Object files for target wrjpgcom
wrjpgcom_OBJECTS = \
"CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o"

# External object files for target wrjpgcom
wrjpgcom_EXTERNAL_OBJECTS =

wrjpgcom: CMakeFiles/wrjpgcom.dir/wrjpgcom.c.o
wrjpgcom: CMakeFiles/wrjpgcom.dir/build.make
wrjpgcom: CMakeFiles/wrjpgcom.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable wrjpgcom"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/wrjpgcom.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/wrjpgcom.dir/build: wrjpgcom
.PHONY : CMakeFiles/wrjpgcom.dir/build

CMakeFiles/wrjpgcom.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/wrjpgcom.dir/cmake_clean.cmake
.PHONY : CMakeFiles/wrjpgcom.dir/clean

CMakeFiles/wrjpgcom.dir/depend:
	cd /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg /home/anarchking/CS50P/project/project/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds/jpeg/arm64-v8a__ndk_target_21/jpeg/CMakeFiles/wrjpgcom.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/wrjpgcom.dir/depend

