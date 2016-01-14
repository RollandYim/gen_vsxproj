import os
import subprocess
import sys

c_include_exts = ['.c', '.cpp', '.cc', '.cxx', '.h', '.hpp', '.hxx', '.inl', '.inc']

def visit(folder):
    global files
    global folders
    for fn in os.listdir(folder):
        filename = os.path.join(folder, fn)
        _, ext = os.path.splitext(fn)
        if os.path.isdir(filename):
            folders.append(filename)
            visit(filename)
        elif ext.lower() in c_include_exts:
            files.append(filename)

files = []
folders = []
indent = 0
proj_guid = ''
vcxproj_guid = ''

def indent_fill():
    global indent
    str = ''
    for i in range(0, indent):
        str += ' '
    return str

def indent_up():
    global indent
    indent += 2

def indent_down():
    global indent
    indent -= 2

def gen_GUID():
    op = subprocess.Popen(['.\\GuidGen.exe', '/u'], stdout=subprocess.PIPE)
    guidstr, _ = op.communicate()
    guidret = str(guidstr)[2:-5]
    print('gen_GUID ' + guidret)
    return guidret

def get_proj_guid():
    global proj_guid
    if (len(proj_guid) < 1):
        proj_guid = gen_GUID()
    return proj_guid

def get_vcxproj_guid():
    global vcxproj_guid
    if (len(vcxproj_guid) < 1):
        vcxproj_guid = gen_GUID()
    return vcxproj_guid

def generate_vcxproj(project_name, code_folder, save_path):
    global files

    file = open(save_path, 'w')

    file.write('<?xml version="1.0" encoding="utf-8"?>\r\n')
    file.write('<Project DefaultTargets="Build" ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">\r\n')

    indent_up()
    file.write(indent_fill() + '<ItemGroup Label="ProjectConfigurations">\r\n')
    indent_up()
    file.write(indent_fill() + '<ProjectConfiguration Include="Debug|Win32">\r\n')
    indent_up()
    file.write(indent_fill() + '<Configuration>Debug</Configuration>\r\n')
    file.write(indent_fill() + '<Platform>Win32</Platform>\r\n')
    indent_down()
    file.write(indent_fill() + '</ProjectConfiguration>\r\n')
    file.write(indent_fill() + '<ProjectConfiguration Include="Release|Win32">\r\n')
    indent_up()
    file.write(indent_fill() + '<Configuration>Release</Configuration>\r\n')
    file.write(indent_fill() + '<Platform>Win32</Platform>\r\n')
    indent_down()
    file.write(indent_fill() + '</ProjectConfiguration>\r\n')
    indent_down()
    file.write(indent_fill() + '</ItemGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<PropertyGroup Label="Globals">\r\n')
    indent_up()
    file.write(indent_fill() + '<ProjectGuid>{' + get_vcxproj_guid() + '}</ProjectGuid>\r\n')
    file.write(indent_fill() + '<Keyword>Win32Proj</Keyword>\r\n')
    file.write(indent_fill() + '<RootNamespace>' + project_name + '</RootNamespace>\r\n')
    indent_down()
    file.write(indent_fill() + '</PropertyGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<Import Project="$(VCTargetsPath)\Microsoft.Cpp.Default.props" />\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<PropertyGroup Condition="\'$(Configuration)|$(Platform)\'==\'Debug|Win32\'" Label="Configuration">\r\n')
    indent_up()
    file.write(indent_fill() + '<ConfigurationType>Application</ConfigurationType>\r\n')
    file.write(indent_fill() + '<UseDebugLibraries>true</UseDebugLibraries>\r\n')
    file.write(indent_fill() + '<CharacterSet>Unicode</CharacterSet>\r\n')
    indent_down()
    file.write(indent_fill() + '</PropertyGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<PropertyGroup Condition="\'$(Configuration)|$(Platform)\'==\'Release|Win32\'" Label="Configuration">\r\n')
    indent_up()
    file.write(indent_fill() + '<ConfigurationType>Application</ConfigurationType>\r\n')
    file.write(indent_fill() + '<UseDebugLibraries>true</UseDebugLibraries>\r\n')
    file.write(indent_fill() + '<CharacterSet>Unicode</CharacterSet>\r\n')
    indent_down()
    file.write(indent_fill() + '</PropertyGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<Import Project="$(VCTargetsPath)\Microsoft.Cpp.props" />\r\n')
    file.write(indent_fill() + '<ImportGroup Label="ExtensionSettings">\r\n')
    file.write(indent_fill() + '</ImportGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<ImportGroup Label="PropertySheets" Condition="\'$(Configuration)|$(Platform)\'==\'Debug|Win32\'">\r\n')
    indent_up()
    file.write(indent_fill() + '<Import Project="$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props" Condition="exists(\'$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props\')" Label="LocalAppDataPlatform" />\r\n')
    indent_down()
    file.write(indent_fill() + '</ImportGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<ImportGroup Label="PropertySheets" Condition="\'$(Configuration)|$(Platform)\'==\'Release|Win32\'">\r\n')
    indent_up()
    file.write(indent_fill() + '<Import Project="$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props" Condition="exists(\'$(UserRootDir)\Microsoft.Cpp.$(Platform).user.props\')" Label="LocalAppDataPlatform" />\r\n')
    indent_down()
    file.write(indent_fill() + '</ImportGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<PropertyGroup Label="UserMacros" />\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<PropertyGroup Condition="\'$(Configuration)|$(Platform)\'==\'Debug|Win32\'">\r\n')
    indent_up()
    file.write(indent_fill() + '<LinkIncremental>true</LinkIncremental>\r\n')
    indent_down()
    file.write(indent_fill() + '</PropertyGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<PropertyGroup Condition="\'$(Configuration)|$(Platform)\'==\'Release|Win32\'">\r\n')
    indent_up()
    file.write(indent_fill() + '<LinkIncremental>true</LinkIncremental>\r\n')
    indent_down()
    file.write(indent_fill() + '</PropertyGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<ItemDefinitionGroup Condition="\'$(Configuration)|$(Platform)\'==\'Debug|Win32\'">\r\n')
    indent_up()
    file.write(indent_fill() + '<ClCompile>\r\n')
    indent_up()
    file.write(indent_fill() + '<PrecompiledHeader>\r\n')
    file.write(indent_fill() + '</PrecompiledHeader>\r\n')
    file.write(indent_fill() + '<WarningLevel>Level3</WarningLevel>\r\n')
    file.write(indent_fill() + '<Optimization>Disabled</Optimization>\r\n')
    file.write(indent_fill() + '<PreprocessorDefinitions>WIN32;_DEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>\r\n')
    indent_down()
    file.write(indent_fill() + '</ClCompile>\r\n')
    file.write(indent_fill() + '<Link>\r\n')
    indent_up()
    file.write(indent_fill() + '<SubSystem>Console</SubSystem>\r\n')
    file.write(indent_fill() + '<GenerateDebugInformation>true</GenerateDebugInformation>\r\n')
    indent_down()
    file.write(indent_fill() + '</Link>\r\n')
    indent_down()
    file.write(indent_fill() + '</ItemDefinitionGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<ItemDefinitionGroup Condition="\'$(Configuration)|$(Platform)\'==\'Release|Win32\'">\r\n')
    indent_up()
    file.write(indent_fill() + '<ClCompile>\r\n')
    indent_up()
    file.write(indent_fill() + '<PrecompiledHeader>\r\n')
    file.write(indent_fill() + '</PrecompiledHeader>\r\n')
    file.write(indent_fill() + '<WarningLevel>Level3</WarningLevel>\r\n')
    file.write(indent_fill() + '<Optimization>Disabled</Optimization>\r\n')
    file.write(indent_fill() + '<PreprocessorDefinitions>WIN32;_DEBUG;_CONSOLE;%(PreprocessorDefinitions)</PreprocessorDefinitions>\r\n')
    indent_down()
    file.write(indent_fill() + '</ClCompile>\r\n')
    file.write(indent_fill() + '<Link>\r\n')
    indent_up()
    file.write(indent_fill() + '<SubSystem>Console</SubSystem>\r\n')
    file.write(indent_fill() + '<GenerateDebugInformation>true</GenerateDebugInformation>\r\n')
    indent_down()
    file.write(indent_fill() + '</Link>\r\n')
    indent_down()
    file.write(indent_fill() + '</ItemDefinitionGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<ItemGroup>\r\n')
    indent_up()
    for fn in files:
        diff_len = len(fn) - len(code_folder)
        rel_fn = fn[-diff_len:]
        file.write(indent_fill() + '<ClCompile Include="' + rel_fn + '"/>\r\n')
    indent_down()
    file.write(indent_fill() + '</ItemGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<Import Project="$(VCTargetsPath)\Microsoft.Cpp.targets" />\r\n')
    file.write(indent_fill() + '<ImportGroup Label="ExtensionTargets">\r\n')
    file.write(indent_fill() + '</ImportGroup>\r\n')
    indent_down()

    file.write('</Project>\r\n')

    file.close()

    print('generate %s ok' % save_path)

def generate_vcxproj_filters(project_name, code_folder, save_path):
    global files
    global folders

    file = open(save_path, 'w')

    file.write('<?xml version="1.0" encoding="utf-8"?>\r\n')
    file.write('<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">\r\n')

    indent_up()
    file.write(indent_fill() + '<ItemGroup>\r\n')
    indent_up()
    for fn in folders:
        diff_len = len(fn) - len(code_folder)
        rel_fn = fn[-diff_len:]
        file.write(indent_fill() + '<Filter Include="' + rel_fn + '"/>\r\n')
    indent_down()
    file.write(indent_fill() + '</ItemGroup>\r\n')
    indent_down()

    indent_up()
    file.write(indent_fill() + '<ItemGroup>\r\n')
    indent_up()
    for fn in files:
        diff_len = len(fn) - len(code_folder)
        rel_fn = fn[-diff_len:]
        rel_dir, _ = os.path.split(rel_fn)
        rel_dir.rstrip('\\')
        file.write(indent_fill() + '<ClCompile Include="' + rel_fn + '">\r\n')
        if len(rel_dir) > 0:
            file.write('  <Filter>' + rel_dir + '</Filter>\r\n')
        file.write(indent_fill() + '</ClCompile>\r\n')
    indent_down()
    file.write(indent_fill() + '</ItemGroup>\r\n')
    indent_down()
    file.write('</Project>\r\n')

    file.close()

    print('generate %s ok' % save_path)

def generate_sln(project_name, code_folder, save_path):
    file = open(save_path, 'w')

    file.write('Microsoft Visual Studio Solution File, Format Version 11.00\r\n')
    file.write('# Visual Studio 2010\r\n')
    file.write('Project("{' + get_proj_guid() + '}") = "' + project_name + '", "' + project_name + '.vcxproj", "{' + get_vcxproj_guid() + '}"\r\n')
    file.write('EndProject\r\n')
    file.write('Global\r\n')

    indent_up()
    file.write(indent_fill() + 'GlobalSection(SolutionConfigurationPlatforms) = preSolution\r\n')
    indent_up()
    file.write(indent_fill() + 'Debug|Win32 = Debug|Win32\r\n')
    file.write(indent_fill() + 'Release|Win32 = Release|Win32\r\n')
    indent_down()
    file.write(indent_fill() + 'EndGlobalSection\r\n')
    file.write(indent_fill() + 'GlobalSection(ProjectConfigurationPlatforms) = postSolution\r\n')
    indent_up()
    file.write(indent_fill() + '{' + get_vcxproj_guid() + '}.Debug|Win32.ActiveCfg = Debug|Win32\r\n')
    file.write(indent_fill() + '{' + get_vcxproj_guid() + '}.Debug|Win32.Build.0 = Debug|Win32\r\n')
    file.write(indent_fill() + '{' + get_vcxproj_guid() + '}.Release|Win32.ActiveCfg = Release|Win32\r\n')
    file.write(indent_fill() + '{' + get_vcxproj_guid() + '}.Release|Win32.Build.0 = Release|Win32\r\n')
    indent_down()
    file.write(indent_fill() + 'EndGlobalSection\r\n')
    indent_up()
    file.write(indent_fill() + 'GlobalSection(SolutionProperties) = preSolution\r\n')
    indent_up()
    file.write(indent_fill() + 'HideSolutionNode = FALSE\r\n')
    indent_down()
    file.write(indent_fill() + 'EndGlobalSection\r\n')
    indent_down()

    file.write('EndGlobal\r\n')

    file.close()

    print('generate %s ok' % save_path)

def main(argv):
    if (len(argv) < 2):
        print('Usage %s code_folder [save_path] [project_name]' % argv[0])
        sys.exit()

    code_folder = argv[1]
    code_folder = code_folder.replace("/", "\\")

    if (len(argv) >= 3):
        save_path = argv[2]
        save_path = save_path.replace("/", "\\")
    else:
        save_path = code_folder

    if (len(argv) >= 4):
        proj_name = argv[3]
    else:
        proj_name = save_path
    seglist = proj_name.rsplit("\\")
    for i in range(len(seglist) - 1, -1, -1):
        if (seglist[i] != "src"):
            proj_name = seglist[i]
            break
    else:
        proj_name = "none"

    save_prefix = save_path + '\\' + proj_name;
    vcx_path = save_prefix + '.vcxproj'
    vcx_filter_path = vcx_path + '.filters'
    sln_path = save_prefix + '.sln'

    if (code_folder[-1] != '\\'):
        code_folder += '\\'

    visit(code_folder)

    generate_vcxproj(proj_name, code_folder, vcx_path)
    generate_vcxproj_filters(proj_name, code_folder, vcx_filter_path)
    generate_sln(proj_name, code_folder, sln_path)

if __name__ == "__main__":
    main(sys.argv)
