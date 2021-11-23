import IFile from './file.model';

interface Directory {
  name: string;
  directories: Directory[];
  files: IFile[];
}

export default Directory;
