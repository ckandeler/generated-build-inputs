import qbs
import qbs.Process

QtApplication {
    cpp.includePaths: [buildDirectory]
    Rule {
        multiplex: true
        inputs: ["geninput", "genscript"]
        outputFileTags: ["hpp"]
        outputArtifacts: {
            var p = new Process;
            try {
                p.exec(inputs["genscript"][0].filePath, ["--list", product.buildDirectory,
                                                         inputs["geninput"][0].filePath], true);
                var artifacts = [];
                var headerFile = p.readLine();
                while (headerFile) {
                    artifacts.push({ filePath: headerFile });
                    headerFile = p.readLine();
                }
                return artifacts;
            } finally {
                p.close();
            }
        }
        prepare: {
            var cmd = new Command(inputs["genscript"][0].filePath,
                                  [product.buildDirectory, inputs["geninput"][0].filePath]);
            cmd.description = "generating header files";
            return [cmd];
        }
    }

    Group {
        name: "generator script"
        fileTags: ["genscript"]
        files: ["generator.py"]
    }

    Group {
        name: "generator input"
        fileTags: ["geninput"]
        files: ["fileWithNumber"]
    }

    files: [
        "CMakeLists.txt",
        "servertest.cpp",
    ]
}
