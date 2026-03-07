{
  description = "Python dev environment with uv + requirements.txt";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:

  let
    systems = [
      "x86_64-linux"
      "aarch64-linux"
      "x86_64-darwin"
      "aarch64-darwin"
    ];

    forEachSystem = nixpkgs.lib.genAttrs systems;

    pythonVersion = "3.13";
  in
  {
    devShells = forEachSystem (system:

      let
        pkgs = import nixpkgs { inherit system; };

        concatMajorMinor =
          v:
          pkgs.lib.pipe v [
            pkgs.lib.versions.splitVersion
            (pkgs.lib.sublist 0 2)
            pkgs.lib.concatStrings
          ];

        python = pkgs."python${concatMajorMinor pythonVersion}";
      in
      {
        default = pkgs.mkShellNoCC {

          venvDir = ".venv";

          packages = [
            python
            pkgs.uv                
            python.pkgs.venvShellHook
          ];

          postShellHook = ''
            echo "Python: ${python.version}"

            if [ -f requirements.txt ]; then
              echo "Installing dependencies with uv..."
              uv pip install -r requirements.txt
            fi
          '';
        };
      }
    );
  };
}
